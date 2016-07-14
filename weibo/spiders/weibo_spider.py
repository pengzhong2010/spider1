import scrapy
import re

class WeiboSpider(scrapy.spiders.Spider):
    name = "weibo"
    # allowed_domains = ["dmoz.org"]
    start_urls = [
        "http://m.weibo.cn/page/json?containerid=1005052059910247_-_FANS&page=1",
        # "http://www.dmoz.org/Computers/Programming/Languages/Python/Resources/"
    ]
    page=2
    def parse(self, response):

        next_flag=0
        error_flag=0
        str1=response.body
        str1=str(str1)
        m1 = re.match(r'.*(\"ok\":1,).*', str1)
        if m1:

            error_flag=1
            print m1.groups()

        m2 = re.match(r'.*(\"count\":[\d]+,).*', str1)
        if m2:
            next_flag=1
            print m2.groups()

        # m3 = re.findall(r'.*(\"id\":[\d]+,).*', str1)
        # if m3:
        #     print m3
        # filename = response.url.split("/")[-2]
        filename = 'weibo1'
        str1=response.url+str1
        with open(filename, 'ab') as f:
            f.write(str1)
        print 'next_flag',next_flag
        if next_flag:
            res=scrapy.Request(url="http://m.weibo.cn/page/json?containerid=1005052059910247_-_FANS&page=2" ,
                           callback=self.after_get)
            return res
    def after_get(self,response):
        str1 = response.body
        str1 = str(str1)
        m1 = re.match(r'.*(\"ok\":1,).*', str1)
        if m1:
            error_flag = 1
            print m1.groups()

        m2 = re.match(r'.*(\"count\":[\d]+,).*', str1)
        if m2:
            next_flag = 1
            print m2.groups()

        # m3 = re.findall(r'.*(\"id\":[\d]+,).*', str1)
        # if m3:
        #     print m3
        # filename = response.url.split("/")[-2]
        filename = 'weibo1'
        str1 = response.url + str1
        with open(filename, 'ab') as f:
            f.write(str1)

        if self.page<10:
            if next_flag:
                self.page=self.page+1
                res=scrapy.Request(url="http://m.weibo.cn/page/json?containerid=1005052059910247_-_FANS&page="+str(self.page),callback=self.after_get)
                return res
