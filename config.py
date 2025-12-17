import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
    
    WEATHER_API_URL = "http://api.openweathermap.org/data/2.5/weather"
    QUOTE_API_URL = "https://zenquotes.io/api/random"

if not Config.OPENWEATHER_API_KEY:
    raise ValueError("⚠️  Error: OPENWEATHER_API_KEY is missing in .env file!")