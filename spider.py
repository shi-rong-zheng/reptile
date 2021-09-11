from bs4 import BeautifulSoup
import re
import urllib.request,urllib.error
import xlwt
import sqlite3

def main():
    baseurl="https://movie.douban.com/top250?start=25&filter="
    #1.爬取网页
    datalist=getData(baseurl)
    savepath=".\\豆瓣电影Top250.xls"
    # 3.保存数据
    #savaData(savepath)

    askURL("https://movie.douban.com/top250?start=25&filter=")


 #爬取网页
def getData(baseurl):
    datalist=[]
    # 2.解析数据
    return datalist

#得到指定一个url的网页内容
def askURL(url):
    headers={  #模拟浏览器头部信息，向豆瓣服务器发送消息
        "User-Agent": "Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 93.0.4577.63Safari / 537.36"
    }   #用户代理，表示告诉豆瓣服务器，我们是什么类型的机器，浏览器
    request=urllib.request.Request(url=url,headers=headers)
    html=""
    try:
        response=urllib.request.urlopen(request)
        html=response.read().decode("utf-8")
        print(html)
    except Exception as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    #return html
#保存数据
def savaData(savepath):
    pass



if __name__=="__main__":
    main()