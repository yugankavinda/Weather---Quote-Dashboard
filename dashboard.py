import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

def get_quote():
    url = "https://zenquotes.io/api/random"
    try:
       response = requests.get(url)
       response.raise_for_status()
       data=response.json()
       quote=data[0]['q']
       author=data[0]['a']
       return f'"{quote}" - {author}'

    except requests.exceptions.RequestException as e:
        return f"Error fetching quote: {e}"
    
def get_weather(city):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        
        return f"The current temperature in {city} is {temp}°C with {description.title()}."
    
    except requests.exceptions.HTTPError as err:
        if response.status_code == 404:
            return f"City '{city}' not found."
        return f"Error fetching weather data: {err}"
    except Exception as e:
        return f"An error occurred: {e}"

def main():
    while True:
        if not API_KEY:
            print("Error: OPENWEATHER_API_KEY is not set in the environment variables.")
            return
        print(f"{get_quote()}\n")
        city = input("Enter city name for weather information: ")
        print(f"Checking weather for {city}...\n")
        print(f"{get_weather(city)}\n")
        print("-" * 40)
    

if __name__ == "__main__":
    main()