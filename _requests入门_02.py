import requests
url="https://fanyi.baidu.com/sug"
s=input("请输入你要翻译的英文单词")
data={
    "kw":s
}

#发送post请求，发送的数据必须放在字典中，通过data参数传递
response=requests.post(url,data=data)
print(response.json())#将服务器返回的内容直接处理成json（）-》dict