
from json import dumps, loads
import requests
import json



search_keyword = 'राजनीति'



url = 'https://bg.annapurnapost.com/api/search?title='+search_keyword

# print(url)

r = requests.get(url)
json_data = r.json()

data = json_data['data']


items = (data.get('items'))

news = {"news" + str(i+1): items[i] for i in range(len(items))}

print(news)

# print(news_json)