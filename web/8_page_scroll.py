import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://shopping.naver.com/home/p/index.naver')

browser.maximize_window()

# search input
browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/input[1]').send_keys("무선마우스")

# search btn
browser.find_element_by_xpath('//*[@id="autocompleteWrapper"]/a[2]').click()

# 스크롤
# 지정한 위치로 스크롤 내리기
browser.execute_script('window.scrollTo(0,1080)')

# 화면 가장 아래로 스크롤 내리기
browser.execute_script('window.scrollTo(0, document.body.scrollHeight)')

# 동적페이지 마지막까지 스크롤 반복 수행
# 2초에 한번씩 스크롤 내리기
interval = 2 

# 현재 문서 높이를 가져온다.
prev_height = browser.execute_script('return document.body.scrollHeight')

while True:
    # 스크롤을 화면 가장 아래로 내림
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')

    time.sleep(interval)

    # 현재 문서 높이 가져와서 저장
    curr_height = browser.execute_script('return document.body.scrollHeight')
    # 직전 높이와 같으면, 높이변화가 없으면 break
    if curr_height == prev_height:
        break

    prev_height = curr_height

browser.execute_script('window.scrollTo(0,0)')

time.sleep(5)

browser.quit()