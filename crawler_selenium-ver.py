from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import getpass

id = input('레진코믹스 계정의 아이디를 입력하세요 : ')
pw = input("레진코믹스 계정의 패스워드를 입력하세요 : ")

driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.lezhin.com/ko/login')
delay = 3
driver.implicitly_wait(delay)

driver.find_element_by_id('login-email').send_keys(id)
driver.find_element_by_id('login-password').send_keys(pw)
driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').click()
time.sleep(5)

url = 'https://www.lezhin.com/ko/comic/waitmrpark/64'
driver.get(url)
time.sleep(3)

soup = BeautifulSoup(driver.page_source, "html.parser")
div_tag = soup.find("div", id="scroll-list")
l = list()
for img in div_tag.find_all("img"):
    l.append(img.get("src").split("/"))
print(l[1][7])
