import requests
import pandas as pd

def fetch_weather():
    url = "https://wttr.in/Nairobi?format=j1"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()

        weather = response.json()

        weather_data = {
            "date": pd.Timestamp.today().normalize(),
            "temperature_C": float(weather["current_condition"][0]["temp_C"]),
            "humidity": int(weather["current_condition"][0]["humidity"]),
            "precipitation_mm": float(weather["current_condition"][0]["precipMM"])
        }

        return pd.DataFrame([weather_data])

    except requests.exceptions.RequestException as e:
        print(f"API Error: {e}")
        return pd.DataFrame()

if __name__ == "__main__":
    print(fetch_weather())