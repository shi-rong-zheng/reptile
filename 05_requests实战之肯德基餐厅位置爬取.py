import requests

# localtion=input("请输入地点:")
i=1
while i<=3:
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    data={
        "cname":"",
        "pid":"",
        "keyword": "北京",
        "pageIndex": i,
        "pageSize": 10
    }
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
    }
    response=requests.post(url=url,data=data,headers=headers)
    data_dic=response.text
    fileNmae="北京"+".text"
    with open(fileNmae,'w',encoding='utf-8') as fp:
        fp.write(data_dic)
    i+=1
    print("爬取完成！")





































