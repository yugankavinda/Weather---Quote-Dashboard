import requests
from config import Config

class WeatherService:
    def __init__(self):
        self.api_key = Config.OPENWEATHER_API_KEY
        self.base_url = Config.WEATHER_API_URL

    def get_weather(self, city):
        params = {'q': city, 'appid': self.api_key, 'units': 'metric'}

        try:
            response = requests.get(self.base_url, params=params)
            response.raise_for_status()
            
            data = response.json()
                        
            weather_desc = data['weather'][0]['description'].title()

            return (
                f"Weather in {data['name']}: {weather_desc}\n"
                f"🌡️  Temp: {data['main']['temp']}°C (Feels like {data['main']['feels_like']}°C)\n"
                f"💧 Humidity: {data['main']['humidity']}%"
            )

        except requests.exceptions.HTTPError:
            return f"City '{city}' not found."
        except Exception as e:
            return f"Error: {e}"