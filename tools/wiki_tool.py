import requests
import urllib.parse

def get_summary(topic: str):
    if not topic:
        return None

    encoded_topic = urllib.parse.quote(topic)

    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{encoded_topic}"

    headers = {
        "User-Agent": "AI-Ops-Assistant/1.0"
    }

    try:
        res = requests.get(url, headers=headers, timeout=5)

        if res.status_code != 200:
            return None

        data = res.json()

        if "extract" in data:
            return data["extract"][:250]

    except Exception:
        return None

    return None
