from langchain_openai import ChatOpenAI

class PlannerAgent:
    def __init__(self, model_name: str, api_base: str, api_key: str):
        self.llm = ChatOpenAI(
            model_name=model_name,
            openai_api_base="http://127.0.0.1:1234/v1",
            openai_api_key="abc123"
        )

    def plan(self, topic: str) -> str:
        prompt = (
            "You are a professional research planner.\n"
            "Break the main topic into 6–10 sub-questions that thoroughly cover the domain,\n"
            "spanning background, current developments, open challenges, stakeholders, and future outlook.\n\n"
            f"Topic: {topic}\n\n"
            "Rules:\n"
            "- Return a numbered list only.\n"
            "- Each item should be a single, crisp question.\n"
            "- Avoid redundancy."
        )
        return self.llm.invoke(prompt).content
