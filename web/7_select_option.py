import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml_select')

browser.switch_to.frame('iframeResult')

# 1 option 선택하기 방법 index활용
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[4]')
elem.click()

# 2 option 선택하기 방법 완전히 일치 text활용
# text()="Audi" / option중에서 text가 Audi인걸 찾음
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[text()="Audi"]')
elem.click()

# 2 option 선택하기 방법 text 값이 부분 일치하는 항목
elem = browser.find_element_by_xpath('//*[@id="cars"]/option[contains(text(), "Au")]')
elem.click()

time.sleep(2)

browser.quit()