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

item = soup.select_one("#__NEXT_DATA__")
item = item.text

dict_result = json.loads(item)
print(dict_result)

with open('kakao.json', 'w', encoding='utf-8') as file:
    json.dump(dict_result, file, ensure_ascii=False, indent='\t')
