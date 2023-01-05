import requests
from bs4 import BeautifulSoup
import json

url = 'https://page.kakao.com/_next/data/2.5.0/landing/ranking/11/117.json?ranking_type=daily&pathParams=11&pathParams=117'

<<<<<<< HEAD
req = requests.get(url)

html = req.text
=======
res = requests.get(url)

html = res.text
>>>>>>> 44cfa75f4c13b450a0219be1cc6c2c3c66659c9d

soup = BeautifulSoup(html, 'html.parser')

books = soup.text

<<<<<<< HEAD
a = json.loads(books)
rank = 1
book_list = []
book_list.append(a)
book_list2 = []

with open('kakao.json', 'w', encoding='utf-8') as file:
    json.dump(book_list, file, ensure_ascii=False, indent="\t")

with open('kakao.json', 'rt', encoding='UTF8') as f:
    data = json.load(f)

my_list = data[0]["pageProps"]["initialState"]["json"]["pagewebLayout"]["entities"]["items"]

for list_item in my_list:
    a = my_list[list_item]
    book_list2.append(a)

print(book_list2)
# https://page.kakao.com/content/48526879

with open('kakao.json', 'w', encoding='utf-8') as file:
    json.dump(book_list2, file, ensure_ascii=False, indent="\t")
=======
index = soup.select("#__next > div > div.flex.w-full.grow.flex-col.px-122pxr > div > div > div > div.flex.w-full.grow.flex-col.py-5px > div > div > div > div > div > div > a > div > div.flex.flex-col > span.font-large2-bold.mb-6pxr.text-el-60.css-0")
titles = soup.select('#__next > div > div.flex.w-full.grow.flex-col.px-122pxr > div > div > div > div.flex.w-full.grow.flex-col.py-5px > div > div > div > div > div > div > a > div > div.flex.flex-col > span.font-medium2.pb-2pxr.text-el-70.line-clamp-2.css-0')
thumbnails = soup.select("#__next > div > div.flex.w-full.grow.flex-col.px-122pxr > div > div > div > div.flex.w-full.grow.flex-col.py-5px > div > div > div > div > div > div > a > div > div.relative.overflow-hidden.rounded-3pxr.mr-16pxr.w-80pxr.shrink-0 > div.relative.h-full.w-full.css-1xvfhdq > img")
genres = soup.select("#__next > div > div.flex.w-full.grow.flex-col.px-122pxr > div > div > div > div.flex.w-full.grow.flex-col.py-5px > div > div > div > div > div > div > a > div > div.flex.flex-col > div > span")
urls = soup.select("#__next > div > div.flex.w-full.grow.flex-col.px-122pxr > div > div > div > div.flex.w-full.grow.flex-col.py-5px > div > div > div > div > div > div > a")



book_list = []
for idx, title, thumbnail, genre, url in zip(index, titles, thumbnails, genres, urls):
    book_dict = {}
    
    book_dict['index'] = idx.text
    book_dict['title'] = title.text  
    book_dict['thumbnail'] = thumbnail['src']
    book_dict['genre'] = genre.text
    detail_url = "https://page.kakao.com"+url['href']
    book_dict['url'] = detail_url
    book_list.append(book_dict)

with open('kakao.json', 'w', encoding='utf-8') as file:
    json.dump(book_list, file, ensure_ascii=False, indent='\t')
>>>>>>> 44cfa75f4c13b450a0219be1cc6c2c3c66659c9d
