"""
1. channel_nums.json 내 value*의 내림차순으로 정렬하여 json 파일로 저장 
*channel_nums.json의 구조: key: 유튜브 채널명 / value: 해당 채널에서 시청한 영상 수 

2. category_name_nums.json 내 value*의 내림차순으로 정렬하여 json 파일로 저장 
*category_name_nums.json의 구조: key: 카테고리명 / value: 해당 카테고리에서 시청한 영상 수 
"""

import json
import _global

def sort(json_name: str):
    """
    json 파일을 value 값(숫자)의 내림차순으로 정렬 후 저장 \n
    json_name: _global.temporary_path에 위치한 json 파일명 \n
    파일명: sorted_ + json_name (원래 json 이름) \n
    """
    # channel_nums.json 정렬
    with open(_global.temporary_path+json_name, "rt", encoding="UTF-8") as json_file:
        data = json.load(json_file)

    sorted_dict = dict(sorted(data.items(), key=lambda item: -1*item[1]))
    
    # 정렬을 완료한 파일 저장
    with open(_global.result_path+"sorted_"+json_name, "w", encoding="UTF-8") as json_file:
        json.dump(sorted_dict, json_file, indent=4,ensure_ascii=False)