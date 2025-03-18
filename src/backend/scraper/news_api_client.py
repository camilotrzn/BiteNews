import requests
from typing import List, Dict
from src.config.settings import NEWS_API_KEY


class newsAPIClient:

    def __init__(self, api_key: str = NEWS_API_KEY):

        self.api_key = NEWS_API_KEY
        self.basicURL = "https://newsapi.org/v2"
    

    def get_top_headliners(self, country, category : str = None) -> List[Dict]:

        endpoint = self.basicURL + "/top-headlines"

        params = {
            "country": country,
            "apiKey": self.api_key,
        }

        if category:
            params["category"] = category

        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            return response.json().get("articles", [])
        else:
            print(f"Error obteniendo headliners: {response.status_code} - {response.text}")
            return []

    def get_by_keyword(self, keyword, sortBy, language, searchIn) -> List[Dict]: 

        endpoint = self.basicURL + "/everything" 

        params = {
            "q": keyword,
            "sortBy": sortBy,
            "language":language,
            "searchIn":searchIn,
            "apiKey": self.api_key,
        }

        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            return response.json().get("articles", [])
        else:
            print(f"Error obteniendo resultados por palabras clave: {response.status_code} - {response.text}")
            return []
        
    def get_for_source(self, source) -> List[Dict]:

        endpoint =  self.basicURL + "/top-headlines"

        params = {
            "sources":source,
            "apiKey":self.api_key,
        }

        response = requests.get(endpoint, params=params)
        if response.status_code == 200:
            return response.json().get("articles", [])
        else:
            print(f"Error obteniendo resultados por palabras clave: {response.status_code} - {response.text}")
            return []



if __name__ == "__main__":

    client = newsAPIClient()

    headlines = client.get_top_headliners(country="us", category="entertainment")
    for article in headlines:
         print(article)

    # headlines = client.get_for_source(source="bbc-news")
    # for article in headlines:
    #     print(f"Title: {article['title']}")
    #     print(f"URL: {article['url']}")
    #     print()

    # everything = client.get_by_keyword(keyword ="Python", sortBy ="popularity", language = "en", searchIn = "title")
    # for article in everything:
    #     print(f"Title: {article['title']}")
    #     print(f"URL: {article['url']}")
    #     print()
