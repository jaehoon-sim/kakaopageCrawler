import requests
from bs4 import BeautifulSoup
import json

url = 'https://page.kakao.com/_next/data/2.5.0/landing/ranking/11/117.json?ranking_type=daily&pathParams=11&pathParams=117'

req = requests.get(url)

html = req.text

soup = BeautifulSoup(html, 'html.parser')

books = soup.text

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
    book_dict = {}
    a = my_list[list_item]
    book_dict['book'] = a
    book_list2.append(book_dict)

print(book_list2)
# https://page.kakao.com/content/48526879

with open('kakao.json', 'w', encoding='utf-8') as file:
    json.dump(book_list2, file, ensure_ascii=False, indent="\t")
