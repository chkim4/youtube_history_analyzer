"""
1. channel_nums.json 내 value*의 내림차순으로 정렬하여 json 파일로 저장 
*channel_nums.json의 구조: key: 유튜브 채널명 / value: 해당 채널에서 시청한 영상 수 

2. category_name_nums.json 내 value*의 내림차순으로 정렬하여 json 파일로 저장 
*category_name_nums.json의 구조: key: 카테고리명 / value: 해당 카테고리에서 시청한 영상 수 
"""

import json

# channel_nums.json 정렬
with open("channel_nums.json", "rt", encoding="UTF8") as json_file:
    data = json.load(json_file)

sorted_channel_nums = dict(sorted(data.items(), key=lambda item: -1*item[1]))

with open("sorted_channel_nums.json", "w", encoding="UTF8") as json_file:
    json.dump(sorted_channel_nums, json_file, indent=4,ensure_ascii=False)

#category_name_nums.json 정렬
with open("category_name_nums.json", "rt", encoding="UTF8") as json_file:
    data = json.load(json_file)

sorted_category_name_nums = dict(sorted(data.items(), key=lambda item: -1*item[1]))

with open("sorted_category_name_nums.json", "w", encoding="UTF8") as json_file:
    json.dump(sorted_category_name_nums, json_file, indent=4,ensure_ascii=False)
