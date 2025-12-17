import sys
import time
from services.quote_service import QuoteService
from services.weather_service import WeatherService

def main():
    print("--- 🌟 Weather & Quote Dashboard 🌟 ---")
    print("Initializing services...")

    try:
        quote_service = QuoteService()
        weather_service = WeatherService()
        print("✅ Services loaded successfully!\n")
    except Exception as e:
        print(f"❌ Initialization Error: {e}")
        print("Please check your .env file and internet connection.")
        sys.exit(1)

    while True:
        print("-" * 50)
        
        print("💡 Quote of the moment:")
        
        print(quote_service.get_random_quote())
        
        print("-" * 20)

        try:
            city = input("\n📍 Enter city name (or type 'exit' to quit): ").strip()
        except KeyboardInterrupt:
            print("\n\nExiting... 👋")
            break

        if city.lower() in ['exit', 'quit']:
            print("Goodbye! 👋")
            break

        if not city:
            print("⚠️  Please enter a valid city name.")
            continue

        print(f"\n🔍 Checking weather for '{city}'...")
        time.sleep(0.8)
        
        weather_info = weather_service.get_weather(city)
        print(f"\n{weather_info}")
        
        time.sleep(1)

if __name__ == "__main__":
    main()