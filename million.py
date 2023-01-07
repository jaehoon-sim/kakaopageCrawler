import requests
from bs4 import BeautifulSoup
import json

url = 'https://page.kakao.com/landing/series/poster/page/landing/207'

res = requests.get(url)
html = res.text

soup = BeautifulSoup(html, 'html.parser')

books = soup.select_one("#__NEXT_DATA__")
books = books.text

a = json.loads(books)
rank = 1
book_list = []

book_list.append(a)

with open('million.json', 'w', encoding='utf-8') as file:
    json.dump(book_list, file, ensure_ascii=False, indent="\t")

with open('million.json', 'rt', encoding='UTF8') as f:
    # Load the JSON data into a Python dictionary
    data = json.load(f)

# Extract the list from the dictionary
my_list = data[0]["props"]["pageProps"]["initialState"]["json"]["landing"]["seriesPoster"]["page/landing/207"]["data"]["list"]

for list_item in my_list:
    # print(list_item["title"], list_item["subtitleList"])
    list_item['rank'] = rank
    rank = rank + 1

with open('million.json', 'w', encoding='utf-8') as file:
    json.dump(my_list, file, ensure_ascii=False, indent="\t")
