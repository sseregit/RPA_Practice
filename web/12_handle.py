import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.maximize_window()

browser.get('https://www.w3schools.com/tags/att_input_type_radio.asp')
# 현재 handle 정보
curr_handle = browser.current_window_handle
print(curr_handle)
browser.find_element_by_link_text('Try it Yourself »').click()

# 모든 핸들 정보를 가지고옴
handles = browser.window_handles
for handle in handles:
    print(handle)
    # 각 핸들로 이동한다
    browser.switch_to.window(handle)
    # 현재 핸들 브라우저의 제목 표시
    print(browser.title)
    print()

# 현재 핸들 종료
print("현재 핸들 닫기")    
browser.close()

# 이전 핸들로 돌아오기
print("처음 핸들로 돌아오기")
browser.switch_to.window(curr_handle)

print(browser.title)

browser.get("https://daum.net")

time.sleep(3)
browser.quit()