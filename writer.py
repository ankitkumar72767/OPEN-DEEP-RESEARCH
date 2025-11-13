from typing import List, Dict, Any
from langchain_openai import ChatOpenAI

class WriterAgent:
    def __init__(self, model_name: str, api_base: str, api_key: str):
        self.llm = ChatOpenAI(
            model_name=model_name,
            openai_api_base=api_base,
            openai_api_key=api_key
        )

    def write_report(self, topic: str, qa_blocks: List[Dict[str, Any]],
                     language: str = "en", mode: str = "short") -> str:

        if not qa_blocks:
            return "⚠️ No data available to write the report."

        def pack(blocks):
            text = []
            for b in blocks:
                text.append(f"Q: {b['question']}")
                for r in b["results"][:1]:
                    title = r.get("title") or r.get("url")
                    snippet = (r.get("content","") or "")[:200]
                    text.append(f"- {title}: {snippet}")
            return "\n".join(text)

        # SHORT or LONG
        if mode == "short":
            instructions = (
                "Write a concise research summary in 6–10 sentences. "
                "Keep factual, clear, well-structured and avoid long paragraphs."
            )
        else:
            instructions = (
                "Write a detailed 600–1200 word research report with sections:\n"
                "1. Introduction\n2. Background\n3. Key Findings\n"
                "4. Multi-Perspective Analysis\n5. Challenges\n6. Future Outlook\n7. Conclusion"
            )

        prompt = (
            f"Write the report in {language}.\n"
            f"Topic: {topic}\n\n"
            f"Data:\n{pack(qa_blocks)}\n\n"
            f"{instructions}"
        )

        try:
            response = self.llm.invoke(prompt, max_tokens=1000)
            return response.content
        except Exception as e:
            return f"⚠️ Report generation failed: {e}"
