# 🌟 Weather & Quote Dashboard

A Python-based interactive dashboard that combines weather information and daily inspirational quotes in one convenient CLI application.

## Features

- 💡 **Random Quote Generator** - Displays an inspirational quote each time you interact with the dashboard
- 🌤️ **Real-time Weather Updates** - Get current weather information for any city worldwide
- 📍 **City Search** - Look up weather details by entering any city name
- ✨ **Beautiful CLI Interface** - User-friendly command-line interface with emojis and formatting

## Getting Started

### Prerequisites

- Python 3.x
- pip (Python package manager)
- An OpenWeather API key (free tier available at [openweathermap.org](https://openweathermap.org/api))

### Installation

1. **Clone or download this repository**

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up environment variables:**
   - Create a `.env` file in the root directory
   - Add your OpenWeather API key:
     ```
     OPENWEATHER_API_KEY=your_api_key_here
     ```

4. **Run the application:**
   ```bash
   python main.py
   ```

## Usage

1. Start the application by running `python main.py`
2. A random inspirational quote will be displayed
3. Enter a city name to check the current weather
4. Type `exit` or `quit` to leave the application

### Example Output

```
--- 🌟 Weather & Quote Dashboard 🌟 ---

💡 Quote of the moment:
"The only way to do great work is to love what you do." - Steve Jobs

📍 Enter city name (or type 'exit' to quit): London

🔍 Checking weather for 'London'...

Weather in London: Partly Cloudy
🌡️  Temp: 12°C (Feels like 10°C)
💧 Humidity: 65%
```

## Project Structure

```
.
├── main.py                 # Main application entry point
├── config.py              # Configuration and API settings
├── requirements.txt       # Project dependencies
├── services/
│   ├── weather_service.py # Weather API integration
│   └── quote_service.py   # Quote API integration
└── README.md             # This file
```

## Dependencies

- **requests** - HTTP library for API calls
- **python-dotenv** - Load environment variables from .env file

See `requirements.txt` for full dependency list with versions.

## APIs Used

- **OpenWeatherMap API** - Provides current weather data
- **ZenQuotes API** - Provides random inspirational quotes

## Configuration

The application reads configuration from:
- `config.py` - API endpoints and settings
- `.env` - Environment variables (API keys)

Make sure your `.env` file contains:
```
OPENWEATHER_API_KEY=your_key_here
```

## Error Handling

- Invalid city names will display a "not found" message
- Missing API keys will trigger an initialization error with instructions
- Network errors are caught and reported gracefully

## License

This project is open source and available for personal and educational use.

## Contributing

Feel free to fork, modify, and improve this project!

## Troubleshooting

**Issue: "OPENWEATHER_API_KEY is missing in .env file"**
- Solution: Create a `.env` file in the root directory with your OpenWeather API key

**Issue: "City not found"**
- Solution: Double-check the city name spelling and try again

**Issue: Connection errors**
- Solution: Verify your internet connection and API key validity
