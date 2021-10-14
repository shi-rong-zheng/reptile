import scrapy
from qiubaiPro.item import QiubaiproItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    def parse(self, response):
        #解析：作者的名称+段子内容
        # list_div=response.xpath('//*[@id="content"]/div/div[2]/div')
        # all_data=[]#存储所有解析到数据
        # for div in list_div:
        #     #xpath返回的是列表，但是列表元素一定是selector类型的对象
        #     #extract可以将Selector对象中data参数存储的字符串提取出来
        #     name=div.xpath('./div[1]/a[2]/h2/text()')[0].extract().strip()
        #     #列表调用了extract之后，则表示将列表中每一个Selector对象中data对应的字符串提取了出来
        #     content=div.xpath('./a/div/span//text()').extract()
        #     content=''.join(content).strip()
        #     # print(name,'\n',content)
        #     # break
        #     dic={
        #         'author':name,
        #         'content':content
        #     }
        #     all_data.append(dic)
        # return all_data
        list_div = response.xpath('//*[@id="content"]/div/div[2]/div')
        for div in list_div:
            #xpath返回的是列表，但是列表元素一定是selector类型的对象
            #extract可以将Selector对象中data参数存储的字符串提取出来
            name=div.xpath('./div[1]/a[2]/h2/text()')[0].extract().strip()
            #列表调用了extract之后，则表示将列表中每一个Selector对象中data对应的字符串提取了出来
            content=div.xpath('./a/div/span//text()').extract()
            content=''.join(content).strip()
            item=QiubaiproItem()
            item["name"]=name
            item["content"]=content

            yield item#将item提交给了管道


















