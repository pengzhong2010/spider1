import scrapy
# from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import re


class LoginSpider(scrapy.spiders.Spider):
    name = "login"
    allowed_domains = ['weibo.com','weibo.cn','sina.com.cn']
    # start_urls=['http://m.weibo.cn']
    surl = 'http://m.weibo.cn'
    page_search_url=''
    start_page=1
    #
    # def parse(self, response):
    #     print 'body'
    #     print response.body
    #     print 'headers'
    #     print response.headers
    #     print 'meta'
    #     print response.meta
    headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip,deflate,sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Host':'m.weibo.cn',
        'Pragma':'no-cache',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 9_1 like Mac OS X) AppleWebKit/601.1.46 (KHTML, like Gecko) Version/9.0 Mobile/13B143 Safari/601.1',
    }
    def start_requests(self):
        return [scrapy.Request(url=self.surl,meta={'cookiejar':0},callback=self.see_home
                               )]

    def see_home(self,response):
        # print 'url'
        # print response.url
        # print 'body'
        # print response.body
        # print 'headers'
        # print response.headers
        # print 'meta'
        print response.meta
        print response.meta['cookiejar']

        next_url = response.xpath('//a[contains(@class,"btn btnWhite")]//@href').extract()
        print 'next_url'
        print next_url[0]

        # print

        return [scrapy.Request(url=next_url[0], meta={'cookiejar':response.meta['cookiejar']},
                               callback=self.see_login
                               )]

    def see_login(self,response):
        # print 'url'
        # print response.url
        # print 'body'
        # print response.body
        # print 'headers'
        # print response.headers
        # print 'meta'
        # print response.meta
        return [scrapy.FormRequest(url="https://passport.weibo.cn/sso/login",
                                   method="POST",
                            formdata={
                                'username': 'hongguangui@gmail.com',
                                'password':'Hell0@123',
                                'savestate':'1',
                                'ec':'0',
                                'pagerefer':'',
                                'entry':'mweibo',
                                'wentry':'',
                                'loginfrom':'',
                                'client_id':'',
                                'code': '',
                                'qq': '',
                                'hff': '',
                                'hfp': ''
                            },
                            meta={'cookiejar': response.meta['cookiejar']},
                            callback=self.after_login)]

    def after_login(self,response):

        # print 'url'
        # print response.url
        # print 'body'
        # print response.body
        # print 'headers'
        # print response.headers
        # print 'meta'
        # print response.meta

        return [scrapy.Request(url='http://m.weibo.cn/home/me?format=cards', meta={'cookiejar': response.meta['cookiejar']},
                               callback=self.see_me
                               )]
    def see_me(self,response):

        # print 'url'
        # print response.url
        # print 'body'
        # print response.body
        # print 'headers'
        # print response.headers
        # print 'meta'
        # print response.meta
        # with open('me', 'ab') as f:
        #     f.write(response.body)
        str1 = response.body
        str1 = str(str1)
        m1 = re.match(r'.*\{\"title\":\"\\u7c89\\u4e1d\",.*\/page.*containerid=([\d]+)_-_FANS.*', str1)
        if m1:
            str2 = m1.groups()[0]
            print str2
            self.page_search_url='http://m.weibo.cn/page/json?containerid='+str2+'_-_FANS&page='
            search_url_tmp=self.page_search_url+str(self.start_page)
            return [scrapy.Request(url=search_url_tmp,
                                   meta={'cookiejar': response.meta['cookiejar']},
                                   callback=self.get_page_info
                                   )]

    def get_page_info(self,response):
        print 'url'
        print response.url
        print 'body'
        print response.body
        print 'headers'
        print response.headers
        print 'meta'
        print response.meta


