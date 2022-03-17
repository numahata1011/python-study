# #-*- coding: utf-8 -*-
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome import service as fs

browser = webdriver.Chrome()

browser.get('https://idm-japan.sakura.ne.jp/ems/')

# 要素(element)を指定
elem_username = browser.find_element_by_id('username-121')

# 文字を入力
elem_username.send_keys('idm-japan')

# 要素(element)を指定
elem_password = browser.find_element_by_id('user_password-121')

# パスワードを入力
elem_password.send_keys('Idmjapan75900805')

elem_login_btn = browser.find_element_by_id('um-submit-btn')

elem_login_btn.click()

sleep(3)

elem_scraping_page = browser.find_element_by_link_text('EMS')

elem_scraping_page.click()
sleep(3)

browser.get('https://idm-japan.sakura.ne.jp/ems/staffmonthly/?setdatestaffmonth=2022/03/01&setstaffid=10')

# print(browser.page_source)

elem_scraping = browser.find_element_by_xpath('/html/body/div[1]/table/tfoot/tr/td[2]').text

print(elem_scraping)