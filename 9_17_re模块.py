import re

#findall:匹配字符串中所有的符合正则的内容
# list=re.findall(r"\d+","我的电话号是：10086，我的女朋友的电话号码是10010")
# print (list)

#fianditer：匹配字符串中所有的内容[返回的是迭代器],从迭代器中拿到内容需要，group()

# list=re.finditer(r"\d+","我的电话号是：10086，我的女朋友的电话号码是10010")
# for i in list:
#     print(i.group())

#search,找到一个结果就返回，返回的结果是match对象，拿数据需要.group()
# s=re.search(r"\d+","我的电话号是：10086，我的女朋友的电话号码是10010")
# print(s.group())

#match是从头开始匹配
# s=re.match(r"\d+","10086，我的女朋友的电话号码是10010")
# print(s.group())

#预加载正则表达式
# obj=re.compile(r"\d+")
# ret=obj.finditer("我的电话是：10086，我女朋友的电话是：10010")
# for it in ret:
#     print(it.group())
# ret=obj.findall("哈哈哈，我就不信你就不还我一个100000000")
# print(ret)

s="""
    <div class='jay'><span id='1'>史荣政</span></div>
    <div class='jj'><span id='2'>何昌俊</span></div>
    <div class='jolin'><span id='3'>钟正彪</span></div>
    <div class='sylar'><span id='4'>徐洪根</span></div>
    <div class='tory'><span id='5'>苏子皓</span></div>
"""

#(?P<分组名字>正则) 可以单独从正则匹配的内容中进一步提取内容
# obj=re.compile(r"<div class='.*?'><span id='(?P<id>\d+)'>(?P<name>.*?)</span></div>",re.S)
#
# result=obj.finditer(s)
# for it in result:
#     print(it.group("id"),end=" ")
#     print(it.group("name"))























































































































