from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# chromedriver.exe 경로를 직접줘도 되고 해당 경로에있으면 상관없음.
browser = webdriver.Chrome()

browser.get("http://naver.com")

# a link의 메일 text를 찾아서 return 해준다.
elem = browser.find_element_by_link_text("메일")

# attribute를 찾는다.
print(elem.get_attribute("href"))

# id중 query를 찾는다.
elem = browser.find_element_by_id("query")
# input에 값을 입력한다.
elem.send_keys("뭐시당가") 
# enter를 입력한다.
elem.send_keys(Keys.ENTER) 
# input을 clear한다
elem.clear()

# element를 클릭한다
elem.click()

# 뒤로가기
browser.back()

# 앞으로 가기
browser.forward()

# 새로고침
browser.refresh()

# 종료하기
browser.quit()