import requests
from bs4 import BeautifulSoup
import json

url = 'https://page.kakao.com/landing/ranking/11/117?ranking_type=daily'

res = requests.get(url)

html = res.text

soup = BeautifulSoup(html, 'html.parser')


index = soup.select("#__next > div > div.flex.w-full.grow.flex-col.px-122pxr > div > div > div > div.flex.w-full.grow.flex-col.py-5px > div > div > div > div > div > div > a > div > div.flex.flex-col > span.font-large2-bold.mb-6pxr.text-el-60.css-1797ph-Text")
titles = soup.select('#__next > div > div.flex.w-full.grow.flex-col.px-122pxr > div > div > div > div.flex.w-full.grow.flex-col.py-5px > div > div > div > div > div > div > a > div > div.flex.flex-col > span.font-medium2.pb-2pxr.text-el-70.line-clamp-2.css-1797ph-Text')
thumbnails = soup.select("#__next > div > div.flex.w-full.grow.flex-col.px-122pxr > div > div > div > div.flex.w-full.grow.flex-col.py-5px > div > div > div > div > div > div > a > div > div.relative.overflow-hidden.rounded-3pxr.mr-16pxr.w-80pxr.shrink-0 > div.relative.h-full.w-full.css-v998tn-Image > img")
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
