import requests
from time import sleep
from selenium import webdriver
bro=webdriver.Chrome(executable_path='F:/下载/chromedriver.exe')
bro.get('http://wlssy.acctedu.com/#/questionMatch')
user=bro.find_element_by_class_name('el-input__inner')
passwd=bro.find_element_by_xpath('/html/body/div/div/div[1]/div/div[1]/div[3]/form/div[2]/div/div[2]/input')
sleep(1)

user.send_keys('gzqgdbd4c01')
sleep(1)
passwd.send_keys('783201')
sleep(1)
btn=bro.find_element_by_xpath('/html/body/div/div/div[1]/div/div[1]/div[3]/form/button')
btn.click()
sleep(1)
span=bro.find_element_by_xpath('/html/body/div/div/div[3]/div/div/div[2]/button/span')
span.click()
sleep(2)
xx=bro.find_elements_by_css_selector('.css-help')[0]
xx.click()
sleep(2)
li=bro.find_elements_by_css_selector('.find_elements_by_css_selector')[0]
li.click()
# page_text=bro.page_source
# print(page_text)
# with open('./xiaobiaobiao.html','w',encoding='utf-8') as fp:
#     fp.write(page_text)