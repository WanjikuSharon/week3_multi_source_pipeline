import requests
import pandas as pd


def fetch_weather_data(start_date: str, end_date: str) -> pd.DataFrame:
    """Fetch date-aligned daily weather data for Nairobi."""
    url = "https://archive-api.open-meteo.com/v1/archive"

    params = {
        "latitude": -1.2921,
        "longitude": 36.8219,
        "start_date": start_date,
        "end_date": end_date,
        "daily": "temperature_2m_mean,precipitation_sum,wind_speed_10m_max",
        "timezone": "Africa/Nairobi",
    }

    try:
        response = requests.get(url, params=params, timeout=15)
        response.raise_for_status()

        payload = response.json()

        if "daily" not in payload or "time" not in payload["daily"]:
            raise ValueError("Expected daily weather data was not returned.")

        daily = payload["daily"]

        return pd.DataFrame({
            "date": pd.to_datetime(daily["time"]),
            "temperature_api_C": daily["temperature_2m_mean"],
            "precipitation_mm": daily["precipitation_sum"],
            "wind_speed_kmh": daily["wind_speed_10m_max"],
        })

    except requests.exceptions.RequestException as exc:
        print(f"Weather API request failed: {exc}")
        return pd.DataFrame()

    except (ValueError, KeyError, TypeError) as exc:
        print(f"Weather API response could not be processed: {exc}")
        return pd.DataFrame()


if __name__ == "__main__":
    today = pd.Timestamp.today().strftime("%Y-%m-%d")
    weather = fetch_weather_data(today, today)

    if weather.empty:
        print("No weather data returned.")
    else:
        print(weather)
