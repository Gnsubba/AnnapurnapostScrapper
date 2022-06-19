
from itertools import count
from json import dumps, loads,dump
import requests

# For tracking page number
page_number = 0

def Scrapper():
    search_keyword = 'राजनीति'

    url = 'https://bg.annapurnapost.com/api/search?title='+search_keyword

    
    # To open the file and check if previously request was sent or not and to retrive page number
    with open('/Users/mac/Documents/web-scraping/AnnapurnapostWebScrapper/data.txt', 'r') as f:
        page_numbers = f.readline()
        if page_numbers == '' or page_numbers == '0':
            page_number = 0
        else:
            print(page_numbers)
            page_number = int(page_numbers)


    # print(url)
    for i in range(3):
        # This is the condition which checks whether the page is already requested and the response was succesful
        if page_number >= i+1:
            break
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

        # To store the news in news.txt
        dump(items, open('news.txt', 'w'))

        page_number = page_number + 1
        print(page_number)

    with open('/Users/mac/Documents/web-scraping/AnnapurnapostWebScrapper/data.txt', 'w') as f:
            f.write(str(page_number))

Scrapper()
