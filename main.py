import requests
import json

url = 'https://page.kakao.com/_next/data/2.5.2/landing/ranking/11/117.json?ranking_type=daily&pathParams=11&pathParams=117'

req = requests.get(url)

data = json.loads(req.text)
rank = 1
book_list = []
book_list.append(data)
book_list2 = []

my_list = data["pageProps"]["initialState"]["json"]["pagewebLayout"]["entities"]["items"]

for list_item in my_list:
    book_dict = {}
    a = my_list[list_item]
    book_dict['book'] = a
    book_dict['book']['link'] = "https://page.kakao.com/content/" + \
        a['eventLog']['eventMeta']['id']
    book_list2.append(book_dict)

# print(book_list2)
# https://page.kakao.com/content/48526879

with open('kakao.json', 'w', encoding='utf-8') as file:
    json.dump(book_list2, file, ensure_ascii=False, indent="\t")
