
from itertools import count
from json import dumps, loads
import requests
import json



search_keyword = 'राजनीति'



url = 'https://bg.annapurnapost.com/api/search?title='+search_keyword

pagination = []

for i in range(3):
    pagination.append(False)

# print(url)
for i in range(3):
    if pagination == True:
        continue
    if i == 0:
        try:
            r = requests.get(url)
        except:
            continue
    else:
        try:
            r = requests.get(url+"&page="+str(i+1))
        except:
            continue
    json_data =r.json()

    data = json_data['data']


    items = (data.get('items'))

    news = {"page"+str(i+1)+"news" + str(j+1): items[j] for j in range(len(items))}

    print(news)
    pagination[i] = True

    # print(news_json)