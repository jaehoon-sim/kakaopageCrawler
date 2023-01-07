import requests
import json

url = "http://page.kakao.com/graphql/"

payload = "{\"query\":\"query seriesPosterViewLandingList($dataKey: String!, $page: Int, $size: Int, $themeKeywordUid: String) {\\r\\n  seriesPosterViewLandingList(\\r\\n    dataKey: $dataKey\\r\\n    page: $page\\r\\n    size: $size\\r\\n    themeKeywordUid: $themeKeywordUid\\r\\n  ) {\\r\\n    id\\r\\n    title\\r\\n    isEnd\\r\\n    totalCount\\r\\n    type\\r\\n    themeKeywordOptList {\\r\\n      param\\r\\n      name\\r\\n      id\\r\\n      __typename\\r\\n    }\\r\\n    selectedThemeKeywordOpt {\\r\\n      param\\r\\n      name\\r\\n      id\\r\\n      __typename\\r\\n    }\\r\\n    list {\\r\\n      id\\r\\n      type\\r\\n      ...PosterViewItem\\r\\n      __typename\\r\\n    }\\r\\n    topImage\\r\\n    __typename\\r\\n  }\\r\\n}\\r\\n\\r\\nfragment PosterViewItem on PosterViewItem {\\r\\n  id\\r\\n  type\\r\\n  showPlayerIcon\\r\\n  scheme\\r\\n  title\\r\\n  thumbnail\\r\\n  badgeList\\r\\n  ageGradeBadge\\r\\n  statusBadge\\r\\n  subtitleList\\r\\n  rank\\r\\n  torosFileHashKey\\r\\n  torosImgId\\r\\n  ageGrade\\r\\n  selfCensorship\\r\\n  eventLog {\\r\\n    ...EventLogFragment\\r\\n    __typename\\r\\n  }\\r\\n  seriesId\\r\\n}\\r\\n\\r\\nfragment EventLogFragment on EventLog {\\r\\n  click {\\r\\n    layer1\\r\\n    layer2\\r\\n    setnum\\r\\n    ordnum\\r\\n    copy\\r\\n    imp_id\\r\\n    imp_provider\\r\\n    __typename\\r\\n  }\\r\\n  eventMeta {\\r\\n    id\\r\\n    name\\r\\n    subcategory\\r\\n    category\\r\\n    series\\r\\n    provider\\r\\n    series_id\\r\\n    type\\r\\n    __typename\\r\\n  }\\r\\n  viewimp_contents {\\r\\n    type\\r\\n    name\\r\\n    id\\r\\n    imp_area_ordnum\\r\\n    imp_id\\r\\n    imp_provider\\r\\n    imp_type\\r\\n    layer1\\r\\n    layer2\\r\\n    __typename\\r\\n  }\\r\\n  customProps {\\r\\n    landing_path\\r\\n    view_type\\r\\n    toros_imp_id\\r\\n    toros_file_hash_key\\r\\n    toros_event_meta_id\\r\\n    content_cnt\\r\\n    event_series_id\\r\\n    event_ticket_type\\r\\n    play_url\\r\\n    banner_uid\\r\\n    __typename\\r\\n  }\\r\\n}\\r\\n\",\"variables\":{\"dataKey\":\"page/landing/207\",\"size\":100}}"
headers = {
    'Content-Type': 'application/json',
    'Cookie': '_kpdid=afb7bf76a65b4e17a16349b104752871'
}

response = requests.request("POST", url, headers=headers, data=payload)

# print(response.text)
rank = 1
data = json.loads(response.text)

my_data = data['data']['seriesPosterViewLandingList']['list']

for list_item in my_data:
    list_item['link'] = "https://page.kakao.com/content/" + \
        list_item['eventLog']['eventMeta']['id']
    list_item['rank'] = rank
    rank = rank + 1

with open('million.json', 'w', encoding='utf-8') as file:
    json.dump(my_data, file, ensure_ascii=False, indent="\t")
