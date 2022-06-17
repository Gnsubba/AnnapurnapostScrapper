from encodings import utf_8
from json import dumps, loads
import requests
import json



search_keyword = 'निर्देशन'

url = 'https://bg.annapurnapost.com/api/search?title='+search_keyword

# print(url)
headers = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.181 Safari/537.36',
    'x-kite-version': '1.2.1',
    'accept': 'application/json, text/plain, */*',
}

r = requests.get(url, headers=headers)
json_data = r.json()

data = json_data['data']


items = (data.get('items'))

news = {"news" + str(i+1): items[i] for i in range(len(items))}

# news_json = dumps(news)

# print(news_json)