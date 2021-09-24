#解析数据
#1.把页面源代码交给BeautifulSoup进行处理，生成bs对象
# page=BeautifulSoup(resp.text,"html.parser")  #指定html解析器
#2.从bs对象中查找数据
#find(标签，属性=值)   找一个
#find_all(标签，属性=值)  找一堆
'''
 -如何实例化BeautifulSoup对象
     -from bs4 import beautifulSoup
     -对象的实例化
        -1.将本地的html文档中的数据加载到该对象中
            fp=open('./sogou.html','r',encoding='utf-8')
            soup=BeautifulSoup(fp,'lxml')
        -2.将互联网上获取的页面源码加载到该对象中
            page_text=response.text
            soup=BeautifulSoup(page_text,'lxml')
    -提供的用于数据解析的方法和属性：
        -soup.tagName:返回的是文档中第一次出现的tanName对应的标签
        -soup.find()：
            -find('tagName'):等同于soup.dib=v
            -属性定位:
                -soup.find('div',class_/id/attr='song')
        -soup.find_all('tagName'):返回符合要求的所有标签（列表）
    -select:
        -select('某种选择器（id，class，标签。。。选择器）'),返回的是一个列表。
        -层级选择器：
            -soup.select('.tang>ul>li>a'):>表示的是一个层级
            -soup.select('.tang>ul a'): 空格表示的多个层级
    -获取标签之间的文本数据：
        -soup.a.text/string/get_text()
        -text/get_text():可以获取某一个标签中所有的文本内容
        -string:值可以获取该标签下面直系的文本内容
    -获取标签中属性值：
        -soup.a['href']
'''
from bs4 import BeautifulSoup
if __name__=='__main__':
    fp=open('./sogou.html','r',encoding='utf-8')
    soup=BeautifulSoup(fp,'lxml')
    print(soup)



