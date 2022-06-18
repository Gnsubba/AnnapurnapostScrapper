
from itertools import count
from json import dumps, loads
import requests
import json



search_keyword = 'राजनीति'



url = 'https://bg.annapurnapost.com/api/search?title='+search_keyword


# print(url)
for i in range(3):
    if i == 0:
        r = requests.get(url)
    else:
        r = requests.get(url+"&page="+str(i+1))
    json_data =r.json()

    data = json_data['data']


    items = (data.get('items'))

    news = {"page"+str(i+1)+"news" + str(j+1): items[j] for j in range(len(items))}

    print(news)

    # print(news_json)