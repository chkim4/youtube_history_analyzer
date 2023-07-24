"""
구글 Takeout 데이터 기반으로 시청한 동영상 분석 \n
분석 내용 (광고 영상 포함, 재생 시간 미반영) \n
  1) 카테고리 별 시청한 동영상 개수 \n
  2) 채널 별 시청한 동영상 게수 \n
"""

import requests
from urllib.parse import urlparse
from urllib.parse import parse_qs
from collections import defaultdict
import os 
import json

# 내가 작성한 모듈
import _global
import generate_json
import sort_json

DEVELOPER_KEY = 'API 키를 입력하세요.'
request_url = "https://www.googleapis.com/youtube/v3/videos?part=snippet&id={id}&key=" + DEVELOPER_KEY

# 아래 3개 변수는 딕셔너리 타입으로 JSON 파일 저장 시 사용. sort_json 이후 삭제함
# category_id_nums: 카테고리 id 별 시청한 동영상 개수 저장
# category_id_name_mapper: 각 카테고리 id와 해당 id의 대응하는 명칭으로 구성된 category_id_name_mapper.json 저장
# channel_nums: 채널 별 시청한 동영상 개수 저장     

category_id_nums = defaultdict(int)
category_id_name_mapper = {}
channel_nums = defaultdict(int)

with open('data/category_id_name_mapper.json') as json_file:
    category_id_name_mapper = json.load(json_file)

with open (_global.URLS, 'r', encoding='UTF8') as urls:  # 파일 불러오기
    for index, url in enumerate(urls):                 # 모든 파일 1줄씩 읽기
        try:
            print("index: ", index)
            print("url: ", url)

            parsed_url = urlparse(url)
            _id = parse_qs(parsed_url.query)['v'][0]

            r = requests.get(request_url.format(id=_id))
            js = r.json()
            items = js["items"][0]

            category_id = items["snippet"]["categoryId"]
            category_id_nums[category_id] += 1
            channel_nums[items['snippet']['channelTitle']] +=1
        
        finally:
            continue

# 정렬이 되지 않은 category_id_nums.json 생성 ({카테고리 id 값: 시청 횟수})
# {카테고리 id :카테고리명}을 저장하는 'category_id_name_mapper.json'을 통해 
# category_num.json{카테고리명: 시청 횟수} 생성
generate_json.generate(category_id_nums, "w","category_id_nums.json")

# 정렬이 되지 않은 category_name_nums 생성 ({카테고리 이름: 시청 횟수})
category_name_nums = {}

for category_id, nums in category_id_nums.items():
    category_name_nums[category_id_name_mapper[category_id]] = nums

generate_json.generate(category_name_nums, "w", "category_name_nums.json")

# 정렬이 되지 않은 channel_nums.json 생성 ({채널명: 시청 횟수})
generate_json.generate(channel_nums, "w", "channel_nums.json")

# 위에서 만든 2개의 json 파일을 정렬
sort_json.sort("channel_nums.json")
sort_json.sort("category_name_nums.json")

# 중간 과정에서 생성된 파일 삭제
os.remove(_global.temporary_path+"category_name_nums.json")
os.remove(_global.temporary_path+"category_id_nums.json")
os.remove(_global.temporary_path+"channel_nums.json")