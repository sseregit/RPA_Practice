import time
from selenium import webdriver

browser = webdriver.Chrome()

# 창최대화
browser.maximize_window()

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

browser.switch_to.frame('iframeResult')

elem = browser.find_element_by_xpath('//*[@id="html"]')

# Radio button 선택 여부 확인
if not elem.is_selected():
    print("선택 안되어있음")
    elem.click()
else:
    print("선택 되어있음")

# Radio button 선택 여부 확인
if not elem.is_selected():
    print("선택 안되어있음")
    elem.click()
else:
    print("선택 되어있음")

time.sleep(3)

browser.quit()