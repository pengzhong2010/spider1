import scrapy
# from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
from scrapy.http import HtmlResponse


class TestSpider(scrapy.spiders.Spider):
    name = "test"
    allowed_domains = ['weibo.com','weibo.cn','sina.com.cn']
    # start_urls=['http://m.weibo.cn']
    # surl = 'http://m.weibo.cn'
    def start_requests(self):
        surl =u'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F'

        return [scrapy.Request(url='http://m.weibo.cn/u/5708787172', meta={'cookiejar': 0}, callback=self.see_home
                               )]

    def see_home(self,response):

        # print 'url'
        # print response.url
        # print 'body'
        # print response.body
        # print 'headers'
        # print response.headers
        # print 'meta'
        with open('one_case', 'ab') as f:
            f.write(response.body)
