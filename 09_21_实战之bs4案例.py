# import requests
# from bs4 import BeautifulSoup
# url='https://www.shicimingju.com/book/sanguoyanyi.html'
# headers={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
# }
# page_text=requests.get(url=url,headers=headers).text
# print(page_text)
# #在首页中解析出章节的标题和详情页的url
# #1.实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
# soup=BeautifulSoup(page_text,'lxml')
# li_list=soup.select('book-mulu>ul>li')
# fp=open("./sanguo.text",'w',encoding='utf-8')
# for li in li_list:
#     titile=li.a.string
#     detail_url='https://www.shicimingju.com/'+li.a['href']
#     # 对详情页发起请求，解析出章节内容
#     detail_page_text=requests.get(url=detail_url,headers=headers).text
#     #解析出详情页中相关的章节内容
#     detail_soup=BeautifulSoup(detail_page_text,'lxml')
#     div_tag=detail_soup.find('div',class_='chapter_content')
#     #解析到了章节的内容
#     content=div_tag.text
#     fp.write(titile+":"+content+'\n')
#     print(titile,'爬取成功！！！')
#
#
import re

#爬取《三国演义》小说
# import requests
# from bs4 import BeautifulSoup
# url='http://sanguo.5000yan.com/'
# headers={
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
#     }
#
# page_text=requests.get(url=url,headers=headers)
# page_text.encoding='utf-8'
# html=page_text.text
# soup=BeautifulSoup(html,'lxml')
# list_li=soup.select('.paiban>li')
# fp=open('./sanguoyanyi.txt','w',encoding='utf-8')
# for i in list_li:
#     #小说名字
#     name=i.a.string
#     #每一章节对应的url
#     url_href=i.a['href']
#     page_href_text=requests.get(url=url_href,headers=headers)
#     page_href_text.encoding='utf-8'
#     data_text=page_href_text.text
#     soup1=BeautifulSoup(data_text,'lxml')
#     div_tag=soup1.find('div',class_="grap")
#     content=div_tag.text
#     # print(content,end='')
#     # break
#     fp.write(name+":"+content+"\n")
#     print(name,"爬取成功！！！")

'''
 xpath解析：最常用且最便捷高效的一种解析方式。通用性。
     -xpath解析原理：
        # -1.实例化一个etree的对象，且需要将被解析的页面源码数据加载到该对象中。
        # -2.调用etree对象中的xpath方法结合着xpath表达式实现标签的定位和内容的捕获。
       -环境的安装：
            -pip install lxml
       -如果实例化一个etree对象
            -1.将本地的html文档中的源码数据加载到etree对象中：
                etree.parse(filePath)
            -2.可以将从互联网上获取的源码数据加载到对象中
                etree.HTML("page_text")
            -xpath('xpath表达式')
       -xpath表达式：
            -/:表示的是从根节点开始定位。表示的是一个层级。
            -//:表示的是多个层级。可以表示从任意位置开始定位。
            -属性定位：//div[@class='song'] tag[@attrName="attrValue"]
            -索引定位：//div[@class='song']/p[3] 索引是从1开始
            -取文本：
                -/text() 获取的是标签中直系的文本内容
                -//text()标签中非直系的文本内容（所有的文本内容）
            -取属性：
                /@ttrName  ==> img/src
            



'''











































































