import requests

#UA伪装
#UA：User-Agent


if __name__=="__main__":
    headers={
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    }
    url='https://www.sogou.com/web?'
    #处理url携带的参数：封装到字典中
    kw=input('enter a word:')
    param={
        "query":kw
    }
    #对指定的url发起的请求对象的url是携带参数的，并且请求过程中处理了参数
    response=requests.get(url=url,params=param,headers=headers)

    page_text=response.text

    fileName=kw+'.html'
    with open(fileName,'w',encoding='utf-8') as fp:
        fp.write(page_text)
    print(fileName,'保存成功！！！')



































