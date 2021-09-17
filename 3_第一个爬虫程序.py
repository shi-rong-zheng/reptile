
from urllib.request import urlopen
url='https://hao.360.com/'
respones=urlopen(url)
# print(respones.read().decode("utf-8"))

with open("mybaidu.html",mode='w',encoding="utf-8") as f:
    f.write(respones.read().decode("utf-8"))
print("over!")