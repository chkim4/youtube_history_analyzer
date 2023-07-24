"""
전역 변수 저장
"""

URLS = "data/urls.txt"
"""
watch-history.html에서 수집한 유튜브 URL을 저장하는 파일명
"""

temporary_path = "temporary/"
"""
정렬이 안 된 json 파일들의 임시 저장 경로. 저장 대상: \n
category_id_nums.json \n
category_name_nums.json, \n
channel_nums.json
"""

result_path = "result/"
"""
정렬이 완료된 최종 json 파일들의 저장 경로. 저장 대상: \n
sorted_channel_nums.json, \n
category_name_nums.json, \n
sorted_category_name_nums.json
"""