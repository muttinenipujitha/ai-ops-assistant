class VerifierAgent:
    def verify(self, results):
        final = {}

        weather = results.get("weather")
        if weather:
            if "error" in weather:
                final["weather"] = weather["error"]
            else:
                final["weather"] = (
                    f"Weather in {weather['city']}, {weather['country']}: "
                    f"{weather['temperature']}°C, "
                    f"Wind {weather['windspeed']} km/h"
                )

        if "news" in results:
            final["news"] = results["news"]

        if "summary" in results and results["summary"]:
            final["about"] = results["summary"]

        return final
