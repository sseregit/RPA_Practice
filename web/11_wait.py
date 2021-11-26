import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome()
browser.get('https://flight.naver.com/')

# 가는날
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[2]/button[1]').click()
time.sleep(2)
days = browser.find_elements_by_css_selector('.num')
days[26].click()
days = browser.find_elements_by_css_selector('.num')
days[29].click()
time.sleep(1)
# 제주 클릭
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[4]/div/div/div[2]/div[1]/button[2]').click()
time.sleep(1)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/section/button[1]').click()
time.sleep(2)
browser.find_element_by_xpath('//*[@id="__next"]/div/div[1]/div[10]/div[2]/section/section/div/button[2]/i[1]').click()
# 검색 클릭
browser.find_element_by_class_name('searchBox_search__2KFn3').click()

# 창이 뜰때 까지 대기하기. 

elem = WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CLASS_NAME,'domestic_results__yNAgI')))

pre_height = browser.execute_script('return document.body.scrollHeight')

while True:
    browser.execute_script(f'window.scrollTo(0,{pre_height})')
    time.sleep(1)
    cur_height = browser.execute_script('return document.body.scrollHeight')

    if pre_height == cur_height:
        break
    
    pre_height = cur_height

tickets = elem.find_elements_by_class_name('result')
for ticket in tickets:
    print(ticket.text)

time.sleep(3)
browser.quit()