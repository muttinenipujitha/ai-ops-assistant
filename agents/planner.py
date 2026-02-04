from llm.llm_client import generate_plan

class PlannerAgent:
    def plan(self, user_task: str):
        return generate_plan(user_task)
