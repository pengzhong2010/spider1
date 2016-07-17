# -*- coding:utf-8 -*-
import scrapy
# from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import re
import time


class DetailSpider(scrapy.spiders.Spider):
    name = "detail"
    allowed_domains = ['weibo.com','weibo.cn','sina.com.cn']
    # start_urls=['http://m.weibo.cn']
    surl = 'http://m.weibo.cn'
    uid_search_home_url='http://m.weibo.cn/u/'
    uid_search_info_url='http://m.weibo.cn/users/'
    uid_catching=0

    uid_info={}
    list_all=[]
    listkey=0
    list_len=0
    num_tmp=0
    str_tmp=''
    uid_filename='uid1_search'
    resjson_filename='weibo6'
    resjson_error_filename='error_detail'
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
        self.list_all=self.get_uid_list()
        self.list_len=len(self.list_all)
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
        list_all=self.get_uid_list()
        # print 'url'
        # print response.url
        # print 'body'
        # print response.body
        # print 'headers'
        # print response.headers
        # print 'meta'
        # print response.meta

        #check res login

        if self.uid_catching:
            # print 'url'
            # print response.url
            # print 'body'
            # print response.body
            # print 'headers'
            # print response.headers
            # print 'meta'
            # print response.meta
            if response.body:
                str1 = response.body
                str1 = str(str1)
                m1 = re.match(
                    r'.*(\<span\>详细资料\<\/span\>.*)\<span id=\"tit_nav\"\>\<\/span\>\<\/nav\>\<section id=\"E_blueV_Company\" class=\"input-info-page\"\>.*',
                    str1)
                if m1:
                    str2 = m1.groups()[0]


                    with open('uid_info3', 'ab') as f:
                        f.write(str2)

                self.uid_catching=0


        if not self.uid_catching:
            self.uid_info={}

            key_tmp=self.listkey
            if key_tmp<self.list_len:

                uid_tmp=self.list_all[key_tmp]
            else:
                uid_tmp=0
            self.listkey=self.listkey+1

            if uid_tmp:
                self.uid_info['uid']=uid_tmp

                search_url_tmp=self.uid_search_home_url+str(uid_tmp)
                return [scrapy.Request(url=search_url_tmp, meta={'cookiejar': response.meta['cookiejar']},
                                       callback=self.uid_home
                                       )]
    def uid_home(self,response):

        # print 'url'
        # print response.url
        # print 'body'
        # print response.body
        # print 'headers'
        # print response.headers
        # print 'meta'
        # print response.meta
        uid_detail_str1=response.body
        uid_detail_str1=str(response.body)

        m1 = re.match(r'.*window\.\$render_data = (.*});.*', uid_detail_str1)
        if m1:
            str1 = m1.groups()[0]
            str2 = str1.replace("\'", '\"')
            with open('uid_home3', 'ab') as f:
                f.write(str2)
            self.uid_info['home']=str2

        if self.uid_info['uid']:
            self.uid_catching=1
            search_url_tmp = self.uid_search_info_url + str(self.uid_info['uid']) +'/?'
            return [scrapy.Request(url=search_url_tmp, meta={'cookiejar': response.meta['cookiejar']},
                                   callback=self.after_login
                               )]

    def get_uid_list(self):
        # f = open('D:\py\weibo\uid1')
        # str1 = f.read()
        #
        # list1 = str1.split("\n")
        # return list1

        list1=[5708787172,5874463817,1333564335,5147470389]
        return list1




