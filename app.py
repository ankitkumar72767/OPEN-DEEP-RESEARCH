import os
import json
import streamlit as st
from dotenv import load_dotenv
from fpdf import FPDF

from backend.graph import ResearchGraph
from backend.utils.citations import flatten_references

load_dotenv()

# -------------------------------------------------------
#  PAGE CONFIG
# -------------------------------------------------------
st.set_page_config(
    page_title="OpenDeepResearcher",
    page_icon="🔎",
    layout="wide"
)

# -------------------------------------------------------
#  UI +  CSS
# -------------------------------------------------------
st.markdown("""
<style>
:root{
    --glass: rgba(255,255,255,0.25);
    --neon: #4f9cff;
    --neon2: #9b5eff;
}

/* global */
html, body, [class*="css"] {
    font-family: "Segoe UI", sans-serif;
    transition: 0.3s ease-in-out;
}

/* navbar */
.navbar {
    padding: 18px;
    text-align: center;
    font-size: 30px;
    font-weight: 900;
    color: white;
    border-radius: 14px;
    background: linear-gradient(90deg, #4f46e5, #2563eb);
    margin-bottom: 15px;
}

/* inputs */
textarea, input {
    background: var(--glass);
    backdrop-filter: blur(12px);
    border-radius: 12px !important;
    border: 1px solid rgba(255,255,255,0.5) !important;
}

textarea:hover, input:hover {
    border-color: var(--neon);
    box-shadow: 0 0 10px var(--neon);
}

/* buttons */
.stButton>button {
    background: linear-gradient(90deg, #4f46e5, #9333ea);
    color: white;
    border-radius: 10px;
    font-size: 17px;
    padding: 10px 20px;
    font-weight: 600;
    border: none;
    transition: 0.25s;
}
.stButton>button:hover {
    transform: scale(1.07);
    box-shadow: 0 8px 30px rgba(147,51,234,0.5);
}

/* report card */
.report-box {
    background: rgba(255,255,255,0.2);
    backdrop-filter: blur(16px);
    padding: 18px;
    border-radius: 14px;
    border: 1px solid rgba(255,255,255,0.4);
}
</style>
""", unsafe_allow_html=True)

# -------------------------------------------------------
#  NAVBAR
# -------------------------------------------------------
st.markdown("<div class='navbar'>🔎 OpenDeepResearcher — AI Agentic Research Assistant</div>", unsafe_allow_html=True)

# -------------------------------------------------------
# SIDEBAR CONFIG
# -------------------------------------------------------
with st.sidebar:
    st.title("⚙️ Configuration")

    api_base = st.text_input("OpenAI API Base", os.getenv("OPENAI_API_BASE", "http://127.0.0.1:1234/v1"))
    api_key = st.text_input("OpenAI API Key", os.getenv("OPENAI_API_KEY", ""), type="password")
    model_name = st.text_input("Model", os.getenv("MODEL_NAME", "qwen2.5-7b-instruct"))
    tavily_key = st.text_input("Tavily API Key", os.getenv("TAVILY_API_KEY", ""), type="password")

    langs = {"English": "en", "Hindi": "hi", "Odia": "or", "Telugu": "te", "Bengali": "bn"}
    lang_choice = st.selectbox("Output Language", list(langs.keys()))

    mode = st.radio("Report Type", ["Short Summary", "Long Academic Report"], index=1)

    max_results = st.slider("Max results per sub-question", 2, 10, 4)

    dl_format = st.selectbox("Download report", ["Markdown (.md)", "JSON (.json)", "PDF (.pdf)"])

# -------------------------------------------------------
#  INPUT
# -------------------------------------------------------
topic = st.text_area("Enter your research topic", height=100)

col1, col2 = st.columns([1,1])
run_click = col1.button(" Run Research", use_container_width=True)
clear_click = col2.button(" Clear History", use_container_width=True)

if clear_click:
    st.session_state["history"] = []
    st.toast(" History cleared")

# -------------------------------------------------------
#  VALIDATION
# -------------------------------------------------------
def validate():
    if not topic.strip(): return "Topic required"
    if not tavily_key.strip(): return "Missing Tavily Key"
    if not api_base.strip(): return "Missing API Base"
    return None

# -------------------------------------------------------
#  RUN PIPELINE
# -------------------------------------------------------
if run_click:
    err = validate()
    if err:
        st.error(err)
    else:
        with st.spinner("⏳ Running multi-agent pipeline..."):
            graph = ResearchGraph(
                model_name=model_name,
                api_base=api_base,
                api_key=api_key,
                tavily_key=tavily_key
            )
            result = graph.run(
                topic,
                max_results=max_results,
                session_id="ui",
                language=langs[lang_choice],
                report_mode="long" if mode == "Long Academic Report" else "short"
            )

        #  Display output
        st.success(" Research Completed!")
        st.subheader(" Research Plan")
        st.code(result["plan"])

        st.subheader("📄 Final Report")
        st.markdown(f"<div class='report-box'>{result['report'].replace(chr(10), '<br>')}</div>",
                    unsafe_allow_html=True)

        #  Prepare references & downloads
        refs = flatten_references(result["qa_blocks"])
        md_report = f"# {topic}\n\n## Introduction\n{result['report']}\n\n## References:\n"
        for r in refs:
            md_report += f"- {r['title']} ({r.get('published_time','')}) → {r['url']}\n"

        json_payload = {
            "topic": topic,
            "report": result["report"],
            "plan": result["plan"],
            "references": refs
        }

        #  PDF export
        def export_pdf(text):
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=11)
            for line in text.split("\n"):
                pdf.multi_cell(0, 7, line)
            return pdf.output(dest="S").encode("latin-1")

        st.markdown("###  Download")
        if dl_format.startswith("Markdown"):
            st.download_button("⬇️ Markdown", md_report, "report.md")
        elif dl_format.startswith("JSON"):
            st.download_button("⬇️ JSON", json.dumps(json_payload, indent=2), "output.json")
        elif dl_format.startswith("PDF"):
            st.download_button("⬇️ PDF", export_pdf(result["report"]), "report.pdf")

        #  Save history
        if "history" not in st.session_state:
            st.session_state["history"] = []
        st.session_state["history"].append({"topic": topic, "report": result["report"]})

# -------------------------------------------------------
# HISTORY
# -------------------------------------------------------
st.markdown("---")
st.subheader("📁 Previous Sessions")

if st.session_state.get("history"):
    for i, h in enumerate(reversed(st.session_state["history"]), start=1):
        preview = h["report"][:280]
        st.markdown(
            f"<div class='history-card'><b>{i}. {h['topic']}</b><br>{preview}...</div>",
            unsafe_allow_html=True
        )
else:
    st.caption("No previous sessions found.")
