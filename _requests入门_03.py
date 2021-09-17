import requests

url="https://movie.douban.com/j/chart/top_list?"

#重新封装参数
param={
    "type": 24,
    "interval_id": "100:90",
    "action":"",
    "start": 0,
    "limit": 20
}

headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}

response=requests.get(url=url,params=param,headers=headers)

print(response.json())

response.close() #关掉response