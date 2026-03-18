import sys
import requests

GEO_URL     = "https://geocoding-api.open-meteo.com/v1/search"
WEATHER_URL = "https://api.open-meteo.com/v1/forecast"

WMO_CODES = {
    0:  "Clear sky",
    1:  "Mainly clear",
    2:  "Partly cloudy",
    3:  "Overcast",
    45: "Fog",
    48: "Icy fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow",
    73: "Moderate snow",
    75: "Heavy snow",
    77: "Snow grains",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    85: "Slight snow showers",
    86: "Heavy snow showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}


def geocode_city(city):
    params = {"name": city, "count": 1, "language": "en", "format": "json"}
    try:
        response = requests.get(GEO_URL, params=params, timeout=10)
    except requests.exceptions.ConnectionError:
        print("no internet or something, can't reach the geocoding api")
        sys.exit(1)
    except requests.exceptions.Timeout:
        print("request took too long, try again")
        sys.exit(1)

    if not response.ok:
        print(f"geocoding api returned {response.status_code}, not sure why")
        sys.exit(1)

    data = response.json()
    results = data.get("results")

    if not results:
        print(f"couldn't find '{city}', maybe check the spelling?")
        sys.exit(1)

    return results[0]


def fetch_weather(lat, lon):
    params = {
        "latitude":        lat,
        "longitude":       lon,
        "current":         "temperature_2m,wind_speed_10m,weather_code",
        "wind_speed_unit": "kmh",
        "timezone":        "auto",
    }
    try:
        response = requests.get(WEATHER_URL, params=params, timeout=10)
    except requests.exceptions.ConnectionError:
        print("can't reach the weather api, check your connection")
        sys.exit(1)
    except requests.exceptions.Timeout:
        print("weather api timed out")
        sys.exit(1)

    if not response.ok:
        print(f"weather api error: {response.status_code}")
        sys.exit(1)

    return response.json()


def display(location, weather):
    current = weather["current"]

    temp_c   = current["temperature_2m"]
    temp_f   = round(temp_c * 9 / 5 + 32, 1)
    wind     = current["wind_speed_10m"]
    code     = current["weather_code"]
    desc     = WMO_CODES.get(code, "unknown")

    city    = location["name"]
    country = location.get("country", "")

    print(f"\ncity: {city}, {country}")
    print(f"temp: {temp_c}C / {temp_f}F")
    print(f"wind: {wind} km/h")
    print(f"condition: {desc}")


def main():
    if len(sys.argv) < 2:
        print("usage: python3 weather.py <city>")
        sys.exit(1)

    city = " ".join(sys.argv[1:])

    location = geocode_city(city)
    weather  = fetch_weather(location["latitude"], location["longitude"])
    display(location, weather)


if __name__ == "__main__":
    main()