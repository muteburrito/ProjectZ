import requests
import json
from bs4 import BeautifulSoup

class Giphy():

    def __init__(self, api_key) -> None:
        self.api_key = api_key

    def construct_params(self, prompt, limit=25, offset=0, rating='g', lang='en', bundle='messaging_non_clips') -> None:
        self.url = f"https://api.giphy.com/v1/gifs/search?api_key={self.api_key}&q={prompt}&limit={limit}&offset={offset}&rating={rating}&lang={lang}&bundle={bundle}"
    
    def get_data(self):
        response = requests.get(self.url)
        self.data = response.json()
        return self.data
    
    def parse_json(self):
        json_data = self.get_data()
        print(type(json_data))
        self.embed_urls = []
        self.titles = []
        self.users = []

        for item in json_data['data']:
            embed_url = item.get('embed_url')
            title = item.get('title')
            user = item.get('username')
            self.embed_urls.append(embed_url)
            self.titles.append(title)
            self.users.append(user)
        
        return self.embed_urls, self.titles, self.users

    def get_gifs(self):
        embed_urls, titles, users = self.parse_json()

        gifs = []
        for embed_url, title, user in zip(embed_urls, titles, users):
            gif = {
                'title': title,
                'embed_url': embed_url,
                'user': user,
            }
            gifs.append(gif)

        return gifs