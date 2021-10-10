from selenium import webdriver
from lxml import etree
from time import sleep
#实例化一个浏览器对象(传入浏览器的驱动器)
bro=webdriver.Chrome(executable_path='F:/下载/chromedriver.exe')
bro.get('http://scxk.nmpa.gov.cn:81/xk/')

#获取浏览器当前页面的源码数据
page_text=bro.page_source

tree=etree.HTML(page_text)
# print(page_text)

li_list=tree.xpath('//*[@id="gzlist"]/li')
for li in li_list:
    name=li.xpath('./dl/@title')[0]
    print(name)

sleep(5)
bro.quit()














