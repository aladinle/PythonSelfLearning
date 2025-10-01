# Weather App (use requests to fetch JSON).

import requests
import sys
import time

# get API key from https://openweathermap.org/current
API_KEY = "5aa6401efa1824ad6cca19cb491933ac";
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def fetch_weather_by_city(city, units="metric", api_key=API_KEY):
    """
    Fetch current weather for `city`.
    units: 'metric' for Celsius, 'imperial' for Fahrenheit, 'standard' for Kelvin
    Returns: dict on success, None on failure
    """
    params = {
        "q" : city,
        "appid" : api_key,
        "units" : units,
    }
    # API call example
    # https://api.openweathermap.org/data/2.5/weather?q={city name}&appid={API key}

    try:
        resp = requests.get(BASE_URL,params=params, timeout=10)
        resp.raise_for_status() # raise HTTPError for bad response
        data = resp.json()
        # Basic sanity check
        if "weather" in data and "main" in data:
            return data
        else:
            print("Unexpected response structure: ", data)
            return None
    except requests.exceptions.HTTPError as e:
        if resp.status_code == 401:
            print("Unauthorized: check your API key.")
        elif resp.status_code == 404:
            print(f"City '{city}' not found.")
        else:
            print("Http error: ", e)
        return None
    except requests.exceptions.Timeout:
        print("Request Time out.")
        return None
    except requests.exceptions.RequestException as e:
        print("Network error: ", e)
        return None

def pretty_print_weather(data, units="metrics"):
     """Nicely format the JSON response for CLI output."""
     if not data:
         print("No data to show.")
         return

     name = data.get("name", "Unknown")
     sys_country = data.get("sys", {}).get("country", "")
     weather = data.get("weather", [{}])[0]
     main = data.get("main", {})
     wind = data.get("wind", {})
     clouds = data.get("clouds", {}).get("all", "N/A")

     temp = main.get("temp", "N/A")
     feels_like = main.get("feels_like", "N/A")
     humidity = main.get("humidity", "N/A")
     pressure = main.get("pressure", "N/A")
     description = weather.get("description", "N/A").capitalize()
     wind_speed = wind.get("speed", "N/A")

     unit_symbol = " C degree" if units == "metric" else " F degree" if units == "imperial" else "K"
     speed_unit = "m/s" if units in ("metric", "standard") else "mph"

     print(f"\nWeather for {name}, {sys_country}")
     print("-" * 30)
     print(f"{description}")
     print(f"Temperature: {temp}{unit_symbol} (feels like {feels_like}{unit_symbol})")
     print(f"Humidity: {humidity}%   Pressure: {pressure} hPa")
     print(f"Wind: {wind_speed} {speed_unit}   Clouds: {clouds}%")
     print("-" * 30)
     # Optionally, print raw JSON timestamp
     dt = data.get("dt")
     if dt:
        print("Data retrieved at:", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(dt)))
     print()

def main():
    if len(sys.argv) > 1:
        city = " ".join(sys.argv[1:])
    else:
        city = input("Enter city name (e.g. London,UK or San Jose,US): ").strip()
        if not city:
            print("City is required.")
            return

    # Choose units
    units = input("Units? (metric/imperial/standard) [metric]: ").strip().lower() or "metric"
    if units not in ("metric", "imperial", "standard"):
        print("Invalid units, defaulting to metric.")
        units = "metric"

    data = fetch_weather_by_city(city, units=units)
    if data:
        pretty_print_weather(data, units=units)

if __name__ == "__main__":
    main()