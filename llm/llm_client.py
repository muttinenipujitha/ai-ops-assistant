import re

def extract_city(task: str):
    """
    Extract city name from phrases like:
    'Get weather in Paris and AI news'
    """
    match = re.search(
        r"weather in ([a-zA-Z\s]+?)(?: and| with|,|$)",
        task,
        re.IGNORECASE
    )
    if match:
        return match.group(1).strip()
    return None


def extract_news_topic(task: str):
    task = task.lower()
    if "ai" in task:
        return "ai"
    if "startup" in task:
        return "startup"
    if "tech" in task or "technology" in task:
        return "technology"
    return "news"


def generate_plan(user_task: str):
    """
    Planner Agent logic:
    Converts user task into structured steps.
    """
    steps = []
    task_lower = user_task.lower()

    if "weather" in task_lower:
        city = extract_city(user_task)
        steps.append({
            "tool": "weather",
            "action": "get_weather",
            "input": {"city": city}
        })

        steps.append({
            "tool": "wiki",
            "action": "get_summary",
            "input": {"topic": city}
        })

    if "news" in task_lower:
        steps.append({
            "tool": "news",
            "action": "get_news",
            "input": {"topic": extract_news_topic(user_task)}
        })

    return {"steps": steps}


