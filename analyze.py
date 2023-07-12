"""
구글 Takeout 데이터 기반으로 시청한 동영상 분석
urls.txt는 여기서 가져옴 (dl 말고 그냥으로 실행)
https://github.com/Jessime/youtube_history

"""

import requests

from urllib.parse import urlparse
from urllib.parse import parse_qs
from collections import defaultdict
from dotenv import load_dotenv
import os 
import json

load_dotenv()

filename = "urls.txt"
DEVELOPER_KEY = os.environ.get('DEVELOPER_KEY')
request_url = "https://www.googleapis.com/youtube/v3/videos?part=snippet&id={id}&key={api_key}"

category_id_nums = defaultdict(int)
category_id_name_mapper = {}
channel_nums = defaultdict(int)

# with open('category_id_name_mapper.json') as json_file:
#     category_id_name_mapper = json.load(json_file)

with open (filename, 'r', encoding='UTF8') as urls:  # 파일 불러내기
    for index, url in enumerate(urls):                 # 모든 파일 1줄씩 읽기
        try:
            print("index: ", index)
            print("url: ", url)

            parsed_url = urlparse(url)
            _id = parse_qs(parsed_url.query)['v'][0]

            r = requests.get(request_url.format(id=_id, api_key=DEVELOPER_KEY))
            js = r.json()
            items = js["items"][0]

            category_id = items["snippet"]["categoryId"]
            category_id_nums[category_id] += 1
            channel_nums[items['snippet']['channelTitle']] +=1
            channel_titles = open("channel_titles.txt", 'a', encoding='utf8')
            channel_titles.write(items['snippet']['channelTitle'])
            channel_titles.write("\n")
            channel_titles.close()
        
        finally:
            continue


with open("category_id_nums.json", "w") as json_file:
    json.dump(category_id_nums, json_file,sort_keys=True, indent=4,ensure_ascii=False)


category_name_nums = {}

for category_id, nums in category_id_nums.items():
    category_name_nums[category_id_name_mapper[category_id]] = nums

print("-------------------------")
print("category_name_nums: " , category_name_nums)

with open("category_name_nums.json", "w") as json_file:
    json.dump(category_name_nums, json_file,sort_keys=True, indent=4,ensure_ascii=False)

print("-------------------------")
print("channel_nums: " , channel_nums)


# 아래 주석은 절대 지우지 말기
# youtube api에서 조회한 category id 리스트를 이용하여 'categoryid: 카테고리 이름' 형태의 json 저장
request_url = "https://www.googleapis.com/youtube/v3/videoCategories?part=snippet&key={api_key}&regionCode=US"
DEVELOPER_KEY = "AIzaSyCKyh2bjMi4iMgKR5lQpgs0tFztkexVNQM"
category_list_json = requests.get(request_url.format(api_key=DEVELOPER_KEY)).json()
category_id_name_mapper = {}

for category_info in category_list_json["items"]:
    category_id_name_mapper[category_info["id"]] = category_info["snippet"]["title"]

with open("category_id_name_mapper.json", "w") as json_file:
    json.dump(category_id_name_mapper, json_file)
# -------------------- 여기까지 지우지 말기 --------------------