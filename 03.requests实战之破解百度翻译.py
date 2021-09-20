import json

import requests
#指定url
url='https://fanyi.baidu.com/sug'
#进行UA伪装
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
dd=input("请输入查找单词:")
#处理url携带的参数：封装到字典中
data={
    "kw":dd
}
#对指定的url发起请求
response=requests.post(url=url,data=data,headers=headers)
dic_json=response.json()
# print(dic_json)

fileName=dd+'.json'
fp=open(fileName,'w',encoding='utf-8')
json.dump(dic_json,fp=fp,ensure_ascii=False)
print("over!!!")




















