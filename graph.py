from typing import Dict, Any
from backend.agents.planner import PlannerAgent
from backend.agents.searcher import SearcherAgent
from backend.agents.writer import WriterAgent
from backend.config import TAVILY_API_KEY, OPENAI_API_BASE, OPENAI_API_KEY, MODEL_NAME
from backend.memory import MemorySaver

class ResearchGraph:
    def __init__(self, model_name: str = MODEL_NAME, api_base: str = OPENAI_API_BASE,
                 api_key: str = OPENAI_API_KEY, tavily_key: str = TAVILY_API_KEY):
        self.memory = MemorySaver()
        self.planner = PlannerAgent(model_name, api_base, api_key)
        self.searcher = SearcherAgent(tavily_key)
        self.writer = WriterAgent(model_name, api_base, api_key)

    def run(self, topic: str, max_results: int = 4, session_id: str = "default",
            language: str = "en", report_mode: str = "short") -> Dict[str, Any]:

        # PLAN
        plan_text = self.planner.plan(topic)
        self.memory.save(session_id, {"stage": "plan", "plan": plan_text})

        # SEARCH
        qa_blocks = []
        for line in plan_text.split("\n"):
            q = line.strip()
            if not q or not any(ch.isalpha() for ch in q):
                continue

            if q[0].isdigit():
                parts = q.split(" ", 1)
                if len(parts) == 2:
                    q = parts[1]

            results = self.searcher.search(q, max_results=max_results)
            qa_blocks.append({"question": q, "results": results})

        self.memory.save(session_id, {"stage": "search", "qa_blocks": qa_blocks})

        # REPORT
        try:
            report = self.writer.write_report(topic, qa_blocks,
                                              language=language, mode=report_mode)
        except Exception as e:
            report = f"⚠️ Report generation failed: {e}"

        self.memory.save(session_id, {"stage": "report", "report": report})

        return {"plan": plan_text, "qa_blocks": qa_blocks, "report": report}
