import requests

def get_weather(city: str):
    if not city:
        return {"error": "No city provided"}

    geo_url = (
        "https://geocoding-api.open-meteo.com/v1/search"
        f"?name={city}&count=1"
    )

    geo_res = requests.get(geo_url).json()

    if "results" not in geo_res or not geo_res["results"]:
        return {"error": f"City '{city}' not found"}

    loc = geo_res["results"][0]
    lat, lon = loc["latitude"], loc["longitude"]

    weather_url = (
        "https://api.open-meteo.com/v1/forecast"
        f"?latitude={lat}&longitude={lon}&current_weather=true"
    )

    weather_res = requests.get(weather_url).json()

    if "current_weather" not in weather_res:
        return {"error": "Weather data unavailable"}

    weather = weather_res["current_weather"]

    return {
        "city": loc["name"],
        "country": loc.get("country", ""),
        "temperature": weather["temperature"],
        "windspeed": weather["windspeed"]
    }
