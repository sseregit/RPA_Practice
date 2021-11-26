import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

result = ("나도","코딩","Canada","퀴즈 완료하였습니다.")

browser = webdriver.Chrome()

browser.get('https://www.w3schools.com/')
browser.maximize_window()

browser.find_element_by_link_text('Learn HTML').click()
browser.find_element_by_link_text('HOW TO').click()
browser.find_element_by_link_text('Contact Form').click()

elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME,'test')))

inputs = elem.find_elements_by_tag_name('input')

for idx,input in enumerate(inputs):
    input.send_keys(result[idx])

elem.find_element_by_xpath(f'//*[@id="country"]/option[text()="{result[2]}"]').click()

text = elem.find_element_by_tag_name('textarea')

text.send_keys(f"{result[3]}")

time.sleep(3)
browser.find_element_by_link_text('Submit').click()

time.sleep(5)
browser.quit()