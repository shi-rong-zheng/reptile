import json

import requests
url='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
headers={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36"
}
#参数的封装
ID_list=[]
for j in range(1,5):
    data={
        "on": "true",
        "page": "j",
        "pageSize": "15",
        "productName":"",
        "conditionType": "1",
        "applyname":""
    }
    response=requests.post(url=url,data=data,headers=headers)
    data_json=response.json()

    # print(data_json["list"])
    list_ID=data_json["list"]

    for i in range(len(list_ID)):
        ID=list_ID[i]["ID"]
        ID_list.append(ID)
url_id='http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
data_dic=[]
for ID in ID_list:
    data1={
       "id":ID
        }
    req=requests.post(url=url_id,data=data1,headers=headers)
    resp=req.json()
    data_dic.append(resp)
    # print(resp["businessLicenseNumber"],end=' ')
    # print(resp['businessPerson'],end=' ')
    # print(resp['certStr'],end=' ')
    # print(resp['epsAddress'],end=' ')
    # print(resp['epsName'],end=' ')
    # print(resp['epsProductAddress'])

fileName='./药监总局'+".json"
fp=open(fileName,'w',encoding='utf-8')
json.dump(data_dic,fp,ensure_ascii=False)
print("爬取完成！！")