import time
from selenium import webdriver
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox')

browser.switch_to.frame('iframeResult')

# elems = browser.find_elements_by_tag_name("input")
# 위와 아래는 같은 역할을 한다.
elems = browser.find_elements(By.TAG_NAME, 'input')

for elem in elems[:-1]:
    if not elem.is_selected():
        print("선택 안되어 있으므로 선택")
        elem.click()
    else:
        print("선택 되어 있으므로 아무것도 안함")

time.sleep(3)