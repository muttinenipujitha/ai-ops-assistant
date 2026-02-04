import requests

def get_news(topic: str):
    url = f"https://hn.algolia.com/api/v1/search?query={topic}"
    res = requests.get(url).json()
    return [hit["title"] for hit in res["hits"][:5]]
