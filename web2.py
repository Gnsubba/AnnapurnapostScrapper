
from itertools import count
from json import dumps, loads
from xmlrpc.client import boolean
import requests
import json



search_keyword = 'राजनीति'



url = 'https://bg.annapurnapost.com/api/search?title='+search_keyword

pagination = []

with open('/Users/mac/Documents/web-scraping/AnnapurnapostWebScrapper/data.txt', 'r') as f:
    if f.readline() == '':
        print("empty file")
    else:
        pagination.append(True)
        for i in range(2):
            pagination.append(eval(f.readline()))

print(pagination)
if pagination.__len__() == 0:
    for i in range(3):
        pagination.append(False)

print(pagination)
# print(url)
for i in range(3):
    if pagination[i] == True:
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

print(pagination)
with open('/Users/mac/Documents/web-scraping/AnnapurnapostWebScrapper/data.txt', 'w') as f:
    for i in range(pagination.__len__()):
        f.write(str(pagination[i]) + '\n')