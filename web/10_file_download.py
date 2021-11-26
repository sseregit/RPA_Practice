import time
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


chrome_options = Options()
chrome_options.add_experimental_option('prefs',{'download.default_directory':os.getcwd()})
browser = webdriver.Chrome(chrome_options=chrome_options)

browser.get('https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_a_download')

browser.switch_to.frame('iframeResult')

# download 링크클릭
elem = browser.find_element_by_xpath('/html/body/p[2]/a/img')
elem.click()

time.sleep(5)

browser.quit()