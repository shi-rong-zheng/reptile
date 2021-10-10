from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.options import Options

from selenium.webdriver import ChromeOptions
#实现无可视化界面的操作
#创建一个参数对象，用来控制chrome以无界面模式打开
chrome_options=Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

#如何实现让selenium规避被检测到的风险
bro=webdriver.Chrome(executable_path='F:/下载/chromedriver.exe',chrome_options=chrome_options)

#无可视化界面（无头浏览器）phantomJs
bro.get('https://www12.baidu.com')

print(bro.page_source)
sleep(2)
bro.quit()





















