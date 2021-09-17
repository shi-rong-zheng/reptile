#拿到页面源代码，requests
#通过re来提取想要的信息
import requests
import re
import csv
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
}
url='https://movie.douban.com/top250'
response=requests.get(url=url,headers=headers)
page_content=response.text

#解析数据
# obj=re.compile(r'<li>.*?<div class="item">.*?<div class="pic">.*?<div class="info">.*?<div class="hd">.*?<span class="title">(?P<name>.*?)</span>',re.S)
# result=obj.finditer(page_content)
# for it in result:
#     print(it.group("name"))
obj=re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">(?P<pf>.*?)</span>.*?<span>(?P<dz>.*?)人评价',re.S)
result=obj.finditer(page_content)

f=open("data.csv",mode="w")
csvwriter=csv.writer(f)

for it in result:
    # print(it.group("year").strip(),end="  ")
    # print(it.group("pf"),end="  ")
    # print(it.group("dz"),end="  ")
    # print(it.group("name"))
    dic=it.groupdict()
    dic['year']=dic['year'].strip()
    csvwriter.writerow(dic.values())
f.close()
print('over!')




























