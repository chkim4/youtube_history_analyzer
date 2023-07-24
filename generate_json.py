"""
파이썬 딕셔너리 파일을 json 파일로 저장
"""
import json

#내가 작성한 모듈
import _global

def generate(_dict: dict , mode: str, json_name: str):
    """
    딕셔너리 타입의 _dict을 불러옴 \n
    mode에 기재된 모드를 통해 \n
    json_name라는 이름의 json 파일로 저장 \n
    """
    json_full_path = _global.temporary_path+json_name
    
    with open(json_full_path, mode, encoding='UTF-8') as json_file:
        json.dump(_dict, json_file,sort_keys=True, indent=4,ensure_ascii=False)

