from tools.weather_tool import get_weather
from tools.news_tool import get_news
from tools.wiki_tool import get_summary

class ExecutorAgent:
    def execute(self, steps):
        results = {}

        for step in steps:
            if step["tool"] == "weather":
                results["weather"] = get_weather(step["input"]["city"])

            if step["tool"] == "news":
                results["news"] = get_news(step["input"]["topic"])

            if step["tool"] == "wiki":
                results["summary"] = get_summary(step["input"]["topic"])

        return results
