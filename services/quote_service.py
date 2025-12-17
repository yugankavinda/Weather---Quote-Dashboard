import requests
from config import Config

class QuoteService:
    def __init__(self):
       self.url=Config.QUOTE_API_URL
    
    def get_random_quote(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()

            raw_data=response.json()
            ext_data=[(data['q'], data['a']) for data in raw_data]
            quote, author=ext_data[0]

            return f'"{quote}" - {author}'

        except requests.exceptions.RequestException as e:
            return f"Error fetching quote: {e}"