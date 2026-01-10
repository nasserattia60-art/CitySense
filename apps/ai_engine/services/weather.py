import requests

def get_weather(lat, lng):
    """
    Fetch current weather from Open-Meteo
    """
    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": lat,
        "longitude": lng,
        "current_weather": True,
        "hourly": "temperature_2m,relativehumidity_2m,windspeed_10m",
        "timezone": "auto"
    }

    response = requests.get(url, params=params)
    data = response.json()

    if "current_weather" not in data:
        return None

    current = data["current_weather"]
    return {
        "temperature": current.get("temperature"),
        "windspeed": current.get("windspeed"),
        "weather_code": current.get("weathercode")  # يمكن تحويله لوصف نصي
    }