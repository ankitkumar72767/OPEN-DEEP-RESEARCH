# 🔎 OpenDeepResearcher — Agentic AI Research Assistant (Streamlit Edition)

OpenDeepResearcher is an AI-powered research tool that behaves like a human researcher.
Give it a topic → it plans, searches, analyzes, and generates a structured research report automatically.

✅ Planner Agent  
✅ Web Search Agent (Tavily)  
✅ Writer Agent (LLM)  
✅ History & Memory  
✅ Beautiful Streamlit UI  
✅ Markdown / JSON / PDF export

---

## ✅ Key Features

- ✅ **Planner Agent** – breaks your topic into smart sub-questions  
- ✅ **Searcher Agent (Tavily API)** – retrieves fresh data from the web  
- ✅ **Writer Agent (LLM)** – writes short or long academic-style reports  
- ✅ **Supports Local Models** – LM Studio / Ollama / OpenAI-compatible APIs  
- ✅ **Session Memory** – saves previous research runs  
- ✅ **Downloads** – Markdown, JSON, PDF  
- ✅ **Clean, modern UI with animations**

---

## ✅ Tech Used

| Component | Technology |
|-----------|------------|
| Frontend UI | Streamlit |
| LLM Framework | LangChain / LangGraph |
| Web Search | Tavily API |
| Local LLM | LM Studio / Ollama |
| Language | Python 3.9+ |

---

## ✅ Folder Structure

OpenDeepResearcher/
│
├── app.py # Streamlit UI
├── backend/
│ ├── graph.py # Research flow (Planner → Search → Writer)
│ ├── memory.py # Session memory tracking
│ ├── agents/
│ │ ├── planner.py
│ │ ├── searcher.py
│ │ └── writer.py
│ └── utils/
│ └── citations.py
├── requirements.txt
└── README.md

yaml
Copy code

---

## ✅ Installation

### 1️⃣ Create Virtual Environment
```bash
python -m venv .venv
Activate:

Windows

bash
Copy code
.venv\Scripts\activate
Linux / Mac

bash
Copy code
source .venv/bin/activate
2️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
3️⃣ Add Environment Variables
You can set them in the terminal or inside .env:

ini
Copy code
TAVILY_API_KEY=your_key_here
OPENAI_API_BASE=http://127.0.0.1:1234/v1
OPENAI_API_KEY=test
For LM Studio / local models, OPENAI_API_KEY can be any placeholder string.

4️⃣ Run the App
bash
Copy code
streamlit run app.py
Then open browser at:

arduino
Copy code
http://localhost:8501
✅ How It Works
You enter a topic

Planner Agent creates sub-questions

Searcher Agent fetches articles with URLs and timestamps

Writer Agent generates a clean research report

You can download the output

✅ Example Output
✔ Research plan
✔ Short or long academic report
✔ References list
✔ Useful for projects, assignments, and analysis

✅ Example Topics
Future of AI in Healthcare

Impact of Climate Change

Cybersecurity Trends

Electric Vehicles in India

Web 3.0 and Blockchain

✅ Current Status
✔ Fully working
✔ UI completed
✔ Works with LM Studio & Tavily
✔ Download options active
✔ Multi-language support

✅ Future Improvements
Better citation formatting (APA / IEEE)

PowerPoint export

More visual charts & graphs

👨‍💻 Author
Ankit Kumar (CS-AIML)
A complete agentic LLM research system with UI, memory, and multi-agent workflow.

✅ License
Free to use, modify, and improve.

⭐ If you like this project, feel free to fork or star ⭐

yaml
Copy code

---

✅ This README looks **professional, internship-ready, GitHub perfect**  
✅ No grammar mistakes  
✅ Clear, structured, modern formatting

If you want, I can also create:

✅ GitHub project description  
✅ Project logo banner  
✅ Demo screenshots section  
✅ Badge icons (Python / Streamlit / LM Studio)

Would you like those added?