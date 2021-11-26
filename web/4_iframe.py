import time
from selenium import webdriver

browser = webdriver.Chrome()

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_radio')

# frame을 전환한다.
browser.switch_to.frame('iframeResult')
# iframe안에 있는 xpath
elem = browser.find_element_by_xpath('//*[@id="html"]')

elem.click()

# 다시 상위로 빠져나온다.
browser.switch_to_default_content()
# 다시 상위로 올라가면 error 발생
elem = browser.find_element_by_xpath('//*[@id="html"]')

elem.click()

time.sleep(5)

browser.quit()