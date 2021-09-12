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

    # askURL("https://movie.douban.com/top250?start=25&filter=")

#影片详情链接的规则
findLink=re.compile(r'<a href="(.*?)">') #创建正则表达式对象，表示规则（字符串的模式）
#影片图片
findImgSrc=re.compile(r'<img src="(.*?)"',re.S)#让换行符包含在字符中
#影片片名
findTitle=re.compile(r'<span class="title">(.*)</span>')
#影片评分
findRating=re.compile(r'<span class="rating_num" property="v:average">(.*)</span>')
#评价人数
findJudge=re.compile(r'<span>(/d*)人评价</span>')
#找到概识
findInq=re.compile(r'<span class="inq">(.*)</span>')
#找到影片的相关内容
findBd=re.compile(r'<p class="">(.*?)</p>',re.S)
#爬取网页
def getData(baseurl):
    datalist=[]
    for i in range(0,10):   #调用获取页面信息的函数10次
        url=baseurl+str(i*25)
        html=askURL(url)    #保存获取到的网页源码

    # 2.逐一解析数据
    soup=BeautifulSoup(html,"html.parser")
    for item in soup.find_all('div',class_="item"):
        # print(item)  #测试，查看电影item全部信息
        data=[]
        item=str(item)
        print(item)
        break
        link=re.findall(findLink,item)[0]    #re库用来通过正则表达式查找指定的字符串
        data.append(link)                    #添加链接
        imgSrc=re.findall(findImgSrc,item)[0]
        data.append(imgSrc)                  #添加图片
        titles=re.findall(findTitle,item)    #片名可能只有一个中文名，没有外国名
        if(len(titles)==2):
            ctitle=titles[0]
            data.append(ctitle)
            otitle=titles[1].replace("/","")  #去掉无关的符号
            data.append(otitle)               #添加外国名
        else:
            data.append(titles[0])
            data.append(' ')                #外国名字留空

        rating=re.findall(findRating,item)[0]
        data.append(rating)                  #添加评分

        judgeNum=re.findall(findJudge,item)[0]
        data.append(judgeNum)                #添加评价人数

        inq=re.findall(findInq,item)
        if len(inq)!=0:
            inq=inq[0].replace("。","")        #去掉句号
            data.append(inq)                   #添加概述
        else:
            data.append(" ")                   #留空

        bd=re.findall(findBd,item)[0]
        bd=re.sub('<br(\s+)?/>(\s+)?'," ",bd)   #去掉<br/>
        bd=re.sub('/'," ",bd)                   #替换/
        data.append(bd.strio())                  #去掉前后的空格

        datalist.append(data)                    #把处理好的一部电影信息放入datalist
    print(datalist)
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
        # print(html)
    except Exception as e:
        if hasattr(e,"code"):
            print(e.code)
        if hasattr(e,"reason"):
            print(e.reason)
    return html
#保存数据
def savaData(savepath):
    pass



if __name__=="__main__":
    main()