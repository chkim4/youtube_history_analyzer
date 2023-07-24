"""
Takout/history/watch-history.html 중 youtube 영상 링크만 별도 저장 \n
링크 모음은 urls.txt 파일로 저장되며 youtube API 호출 시 사용함.
"""
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from pathlib import Path

#내가 작성한 모듈
import _global

YOUTUBE_URL_PATTERN = 'https://www.youtube.com/watch?v='
"""
youtube의 url 패턴. \n
watch-history.html 파일 내 <a> 중에는 href 값이 youtube 영상이 아닌 것도 있음 \n
ex. <a href="googleaccount">
"""

WATCH_HISOTRY_DiRECTORY = './data/watch-history.html'
"""
watch-history.html 경로
"""

def generate_urls(): 
    service = Service(executable_path="/usr/local/bin/chromedriver")
    base_path = Path(__file__).parent
    file_path = (base_path / WATCH_HISOTRY_DiRECTORY)

    with webdriver.Chrome(service=service) as driver:

        #href_pattern: //a[contains(@href, 'https://www.youtube.com/watch?v=')]"  
        href_pattern = "//a[contains(@href, '" + YOUTUBE_URL_PATTERN + "')]"

        driver.get(str(file_path)) 
        a_tags = driver.find_elements(By.XPATH, href_pattern)
      
        for a_tag in a_tags:
            with open(_global.URLS, 'a') as f:
                f.write(a_tag.get_attribute("href"))
                f.write('\n')