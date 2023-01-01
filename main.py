import requests
from bs4 import BeautifulSoup
import json

url = 'https://page.kakao.com/landing/ranking/11/117?ranking_type=daily'

req_header_dict = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'
}

res = requests.get(url, headers=req_header_dict)

html = res.text

soup = BeautifulSoup(html, 'html.parser')


kakaoList = []
detailList = []
detail_list = []
items = soup.select(
    "#__next > div > div.flex.w-full.grow.flex-col.px-122pxr > div > div > div > div.flex.w-full.grow.flex-col.py-5px > div > div > div > div > div > div > a > div > div.flex.flex-col > span.font-medium2.pb-2pxr.text-el-70.line-clamp-2.css-1797ph-Text")


for e, item in enumerate(items, 1):
    kakao_dict = {}
    # print(item.text)
    kakao_dict['title'] = item.text
    kakao_dict['index'] = e
    kakaoList.append(kakao_dict)

for idx, book in enumerate(kakaoList, 1):
    detail_dict = {}
    book_thumbs = soup.select_one(
        "#__next > div > div.flex.w-full.grow.flex-col.px-122pxr > div > div > div > div.flex.w-full.grow.flex-col.py-5px > div > div > div > div > div > div > a > div > div.relative.overflow-hidden.rounded-3pxr.mr-16pxr.w-80pxr.shrink-0 > div.relative.h-full.w-full.css-v998tn-Image > img")['src']
    detail_dict['index'] = book['index']
    detail_dict['title'] = book['title']
    detail_dict['thumbnail'] = book_thumbs
    detailList.append(detail_dict)

for idx, book in enumerate(detailList, 1):
    detail_final_dict = {}
    urls = soup.select_one(
        "#__next > div > div.flex.w-full.grow.flex-col.px-122pxr > div > div > div > div.flex.w-full.grow.flex-col.py-5px > div > div > div > div > div > div > a").get('href')
    detail_final_dict['index'] = book['index']
    detail_final_dict['title'] = book['title']
    detail_final_dict['thumbnail'] = book['thumbnail']
    detail_final_dict['url'] = "https://page.kakao.com"+urls
    detail_list.append(detail_final_dict)


# print(detail_list)


with open('kakao.json', 'w', encoding='utf-8') as file:
    json.dump(detail_list, file, ensure_ascii=False, indent='\t')
