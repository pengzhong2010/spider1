import scrapy
# from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import re
import time

from rec_driver import *
# from pyredis import RedisKv

from pymysql import PyMysql


class LoginSpider(scrapy.spiders.Spider):
    name = "login"
    allowed_domains = ['weibo.com','weibo.cn','sina.com.cn']
    # start_urls=['http://m.weibo.cn']
    surl = 'http://m.weibo.cn'
    page_search_url=''
    start_page=1
    run_page=0
    uid_tmp_list=[]
    uid_write_num=99
    uid_num_tmp=0
    uid_str_tmp=''
    write_num=99
    num_tmp=0
    str_tmp=''
    uid_filename='uid186'
    resjson_filename='weibo186'
    resjson_error_filename='error186'

    mysql_con=''
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

        self.mysql_con = PyMysql(conf1.MYSQL_URL, conf1.MYSQL_PORT, conf1.MYSQL_USER, conf1.MYSQL_PASSWD, conf1.MYSQL_DG_DB)

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

        # return [scrapy.FormRequest(url="https://passport.weibo.cn/sso/login",
        #                            method="POST",
        #                     formdata={
        #                         'username': 'hongguangui@gmail.com',
        #                         'password':'Hell0@123',
        #                         'savestate':'1',
        #                         'ec':'0',
        #                         'pagerefer':'',
        #                         'entry':'mweibo',
        #                         'wentry':'',
        #                         'loginfrom':'',
        #                         'client_id':'',
        #                         'code': '',
        #                         'qq': '',
        #                         'hff': '',
        #                         'hfp': ''
        #                     },
        #                     meta={'cookiejar': response.meta['cookiejar']},
        #                     callback=self.after_login)]

        return [scrapy.FormRequest(url="https://passport.weibo.cn/sso/login",
                               method="POST",
                               formdata={
                                   'username': '18639919430',
                                   'password': 'aaa333',
                                   'savestate': '1',
                                   'ec': '0',
                                   'pagerefer': '',
                                   'entry': 'mweibo',
                                   'wentry': '',
                                   'loginfrom': '',
                                   'client_id': '',
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
            self.run_page=self.start_page

            search_url_tmp=self.page_search_url+str(self.run_page)
            return [scrapy.Request(url=search_url_tmp,
                                   meta={'cookiejar': response.meta['cookiejar']},
                                   callback=self.get_page_info
                                   )]

    def get_page_info(self,response):
        next_flag = 0
        error_flag = 0
        str1 = response.body
        str1 = str(str1)
        m1 = re.match(r'.*(\"ok\":1,).*', str1)
        if not m1:
            error_flag = 1
            # print m1.groups()

        m2 = re.match(r'.*(\"count\":[\d]+,).*', str1)
        if m2:
            next_flag = 1
            # print m2.groups()

        m3 = re.findall(r'\"id\":([\d]+),', str1)
        if m3:
            # print 'm3'
            # print m3
            for i in m3:
                self.uid_tmp_list.append(int(i))
                i_tmp_str = str(i) + "\r\n"
                self.uid_num_tmp = self.uid_num_tmp + 1
                self.uid_str_tmp = self.uid_str_tmp + i_tmp_str
                if self.uid_num_tmp > self.uid_write_num:

                    #add db
                    self.insert_uid()

                    with open(self.uid_filename, 'ab') as f:
                        f.write(self.uid_str_tmp)
                    self.uid_str_tmp = ''
                    self.uid_num_tmp = 0
                    self.uid_tmp_list=[]
                # with open(self.uid_filename, 'ab') as f:
                #     f.write(i_tmp_str)

        str1 = response.url + "---" + "\r\n" + str1 + "\r\n"

        self.num_tmp = self.num_tmp + 1
        self.str_tmp = self.str_tmp + str1
        if self.num_tmp > self.write_num:
            # filename = 'weibo4'
            time_now = time.strftime('%Y-%m-%d %X', time.gmtime(time.time()))
            self.str_tmp = time_now + "----" + "\r\n" + self.str_tmp
            with open(self.resjson_filename, 'ab') as f:
                f.write(self.str_tmp)
            self.str_tmp = ''
            self.num_tmp = 0

        if error_flag:
            time_now = time.strftime('%Y-%m-%d %X', time.gmtime(time.time()))
            str_error = time_now + "----" + "\r\n" + str1
            with open(self.resjson_error_filename, 'ab') as f:
                f.write(str_error)

        if not next_flag:
            time_now = time.strftime('%Y-%m-%d %X', time.gmtime(time.time()))
            self.str_tmp = time_now + "----" + "\r\n" + self.str_tmp
            self.str_tmp = self.str_tmp + 'finished' + '-----' + "\r\n"
            with open(self.resjson_filename, 'ab') as f:
                f.write(self.str_tmp)
            self.str_tmp = ''
            self.num_tmp = 0

            self.insert_uid()
            with open(self.uid_filename, 'ab') as f:
                f.write(self.uid_str_tmp)
            self.uid_str_tmp = ''
            self.uid_num_tmp = 0

        else:
            self.run_page=self.run_page+1
            search_url_tmp = self.page_search_url + str(self.run_page)
            return [scrapy.Request(url=search_url_tmp,
                                   meta={'cookiejar': response.meta['cookiejar']},
                                   callback=self.get_page_info
                                   )]


    def insert_uid(self):
        if not self.uid_tmp_list:
            return
        t_tuple=[]
        for i in self.uid_tmp_list:
            t_tuple_tmp = tuple([i])
            t_tuple.append(t_tuple_tmp)

        sql = """
            insert into weibo_fensi_info (
                `uid`
            ) values (%s)

        """
        ret = self.mysql_con.excute(sql, "many", t_tuple)

        print ret


