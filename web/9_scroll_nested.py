import time
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

browser = webdriver.Chrome()

browser.get('https://www.w3schools.com/html/')

browser.maximize_window()

time.sleep(5)

# 특정 영역 스크롤
# 굳이 click 하는것에 스크롤이 필요하진 않음.
elem = browser.find_element_by_xpath('//*[@id="leftmenuinnerinner"]/a[62]')

# 방법 1 ActionChain
actions = ActionChains(browser)
actions.move_to_element(elem).perform()

# 방법 2
# 함수가 아님 () 필요없음 좌표정보 return
xy = elem.location_once_scrolled_into_view
elem.click()

time.sleep(5)
browser.quit()