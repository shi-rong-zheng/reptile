# 安装requests
import requests
url='https://www.sogou.com/web?query=%E5%91%A8%E6%9D%B0%E4%BC%A6'
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
}
response=requests.get(url=url,headers=headers) #处理一个小小的反爬
print(response.text)














