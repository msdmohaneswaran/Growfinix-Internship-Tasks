
import requests

# ==========================================
# GROWFINIX - EXTERNAL API CONSUMER
# WEATHER INFORMATION APPLICATION
# ==========================================

def get_weather_description(code):

    weather_codes = {
        0: "Clear sky",
        1: "Mainly clear",
        2: "Partly cloudy",
        3: "Overcast",
        45: "Foggy",
        48: "Foggy",
        51: "Light drizzle",
        53: "Moderate drizzle",
        55: "Heavy drizzle",
        61: "Light rain",
        63: "Moderate rain",
        65: "Heavy rain",
        71: "Light snow",
        73: "Moderate snow",
        75: "Heavy snow",
        80: "Rain showers",
        81: "Moderate rain showers",
        82: "Heavy rain showers",
        95: "Thunderstorm"
    }

    return weather_codes.get(code, "Unknown weather")


def get_city_coordinates(city):

    url = "https://geocoding-api.open-meteo.com/v1/search"

    params = {
        "name": city,
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(url, params=params, timeout=15)
    response.raise_for_status()

    data = response.json()

    if "results" not in data or not data["results"]:
        return None

    return data["results"][0]


def get_weather(city):

    try:
        # Step 1: Find city coordinates
        location = get_city_coordinates(city)

        if location is None:
            print("\nCity not found. Please try another city.")
            return

        latitude = location["latitude"]
        longitude = location["longitude"]

        # Step 2: Connect to weather API
        url = "https://api.open-meteo.com/v1/forecast"

        params = {
            "latitude": latitude,
            "longitude": longitude,
            "current": "temperature_2m,relative_humidity_2m,weather_code,wind_speed_10m",
            "timezone": "auto"
        }

        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()

        data = response.json()

        # Step 3: Extract JSON information
        current = data["current"]

        temperature = current["temperature_2m"]
        humidity = current["relative_humidity_2m"]
        wind_speed = current["wind_speed_10m"]
        code = current["weather_code"]

        weather = get_weather_description(code)

        # Step 4: Display results
        print("\n" + "=" * 45)
        print("       GROWFINIX WEATHER APPLICATION")
        print("=" * 45)

        print("City          :", location["name"])
        print("Country       :", location.get("country", "Unknown"))
        print("Temperature   :", temperature, "°C")
        print("Humidity      :", humidity, "%")
        print("Wind Speed    :", wind_speed, "km/h")
        print("Weather       :", weather)

        print("=" * 45)
        print("       WEATHER FETCH SUCCESSFUL")
        print("=" * 45)

    except requests.exceptions.Timeout:
        print("\nError: API request timed out.")

    except requests.exceptions.RequestException as error:
        print("\nNetwork/API Error:", error)

    except (KeyError, ValueError) as error:
        print("\nError processing API data:", error)


def main():

    print("=" * 45)
    print("       GROWFINIX WEATHER APPLICATION")
    print("=" * 45)

    city = input("\nEnter city name: ").strip()

    if not city:
        print("Please enter a valid city name.")
        return

    get_weather(city)


if __name__ == "__main__":
    main()
