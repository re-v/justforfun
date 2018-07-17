import time
from selenium import webdriver
__author__ = 're_v'

url = 'https://weibo.com/u/5340337769?from=myfollow_all&is_all=1'

def start_chrome():
    driver = webdriver.Chrome(executable_path='./chromedriver.exe')
    driver.start_client()
    return driver

def find_info():
    sel = 'span > span.line.S_line1 > span > em:nth-child(2)'
    elements = driver.find_elements_by_css_selector(sel)
    return [el.text for el in elements]
while True:
    driver = start_chrome()
    driver.get(url)
    time.sleep(5)#wait for loading
    info = find_info()
    time.sleep(1200)#稳定性