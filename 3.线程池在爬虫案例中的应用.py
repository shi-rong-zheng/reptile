from multiprocessing import Pool
import requests
import os
from lxml import etree
#爬取梨视频的视频数据
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
#原则：线程池处理的是阻塞且耗时的操作

#对下述url发起请求解析出视频详情页的url和视频的名称
url='https://www.qiushibaike.com/video/'
page_text=requests.get(url=url,headers=headers).text
tree=etree.HTML(page_text)
list_div=tree.xpath('//*[@id="content"]/div/div[2]/div')
if not os.path.exists("./qiutump4"):
    os.mkdir("./qiutump4")
urls=[]
for src in list_div:
    src_url="https:"+src.xpath('./video[@controls="controls"]/source/@src')[0]
    name=src.xpath('./a/div/span/text()')[0].strip()
    # print(src_url,name)
    dic={
        "name":name,
        "url":src_url
    }
    urls.append(dic)
# def get_data(dic):
    url=dic["url"]
    data=requests.get(url=url,headers=headers).content
    Path="./qiutump4/"+name+".mp4"
    with open(Path,"wb") as fp:
        fp.write(data)
        print(dic['name'],"爬取完成！！！")
# pool=Pool(10)
# pool.map(get_data,urls)
#
# pool.close()
# pool.join()































