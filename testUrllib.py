import urllib.request
#获取一个get请求
# response=urllib.request.urlopen("http://www12.baidu.com")
# print(response.read().decode('utf-8'))#对获取到的网页源码进行utf-8解码


#获取一个post请求
# import urllib.parse
# data=bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response=urllib.request.urlopen("http://www.httpbin.org/post",data=data)
# print(response.read().decode('utf-8'))

# try:
#     response=urllib.request.urlopen("http://www.httpbin.org/get",timeout=0.1)
#     print(response.read().decode("utf-8"))
# except Exception as orr:
#     print(orr)

# response=urllib.request.urlopen("http://www.baidu.com")
# print(response.status)
# print(response.read().decode("utf-8"))
# print(response.getheaders())

'''
url="http://www.httpbin.org/post"
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}
data=bytes(urllib.parse.urlencode({"name":"eric"}),encoding="utf-8")
req=urllib.request.Request(url=url,data=data,headers=headers,method="POST")
response=urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
'''
'''
url="https://movie.douban.com/top250?start=25&filter="
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36'
}
res=urllib.request.Request(url=url,headers=headers)
respones=urllib.request.urlopen(res)
print(respones.read().decode("utf-8"))
'''









