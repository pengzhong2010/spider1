# -*- coding:utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
# from scrapy.http import HtmlResponse
import re
import time

from rec_driver import *
# from pyredis import RedisKv

from pymysql import PyMysql
import common


class WebpconeSpider(scrapy.spiders.Spider):
    name = "webpcone"
    appid = 1287792
    allowed_domains = ['weibo.com', 'weibo.cn', 'sina.com.cn']
    # start_urls=['http://m.weibo.cn']
    spider_sep_per_time = 600

    surl = 'http://weibo.com/2714280233/follow?from=page_100505&wvr=6&mod=headfollow#place'

    login_uid = 0
    uid_tmp_list = []

    next_page=0
    largest_page=50

    mysql_con = ''
    error_file_dir = ""
    error_file = ''

    my_headers = {}
    my_cookies = {}

    def shell_init(self):
        self.error_file_dir=conf1.error_file_dir
        self.error_file=self.name+'_error'

    def start_requests(self):
        self.shell_init()
        self.next_page=self.largest_page
        cookies_list = common.read_cookie(self.name, conf1.PAPI_COOKIES).split('; ')

        for i in cookies_list:
            tmp = i.split('=')

            k = tmp[0]

            v = tmp[1]

            self.my_cookies.setdefault(k, v)

        self.mysql_con = PyMysql(conf1.MYSQL_URL, conf1.MYSQL_PORT, conf1.MYSQL_USER, conf1.MYSQL_PASSWD,
                                 conf1.MYSQL_DG_DB)

        return [scrapy.Request(url=self.surl, meta={'cookiejar': 0}, cookies=self.my_cookies, callback=self.see_home
                               )]

    def see_home(self, response):


        # print 'url'
        # print response.url
        # print 'body'
        # print response.body
        # print 'headers'
        # print response.headers
        # print 'meta'
        # print response.meta
        #
        # with open('webpage', 'ab') as f:
        #     f.write(response.body)

        if not common.login_filter(self.error_file_dir, self.error_file, response.url):
            return

        # response.xpath('')
        url_tmp = response.url
        url_tmp = str(url_tmp)
        m1 = re.match(r'.*\/(\d+)\/.*', url_tmp)
        if m1:
            self.login_uid = m1.groups()[0]

            # url_fans='http://weibo.com/' + str(self.login_uid) + '/fans?rightmod=1&wvr=6'
            url_fans = 'http://weibo.com/2714280233/fans?cfs=600&relate=fans&t=1&f=1&type=&Pl_Official_RelationFans__103_page='+str(self.largest_page)+'#Pl_Official_RelationFans__103'
            # print "next_url"
            # print url_fans

            return [scrapy.Request(url=url_fans, meta={'cookiejar': 0}, cookies=self.my_cookies, dont_filter=True, callback=self.see_list
                                   )]

    def see_list(self, response):

        # print 'url'
        # print response.url
        # print 'body'
        # print response.body
        # print 'headers'
        # print response.headers
        # print 'meta'
        # print response.meta
        #
        # with open('fans_list', 'ab') as f:
        #     f.write(response.body)

        if not common.login_filter(self.error_file_dir, self.error_file, response.url):
            return
        common.stay_cookie(self.name, response.request.headers.getlist('Cookie')[0])

        str1 = response.body
        str1 = str(str1)
        str2 = str1.replace("\n", "")
        str2 = str2.replace("\\n", "")
        m1 = re.match(r'.*\<!--粉丝列表--\>(.*)', str2)
        if m1:

            str2 = m1.groups()[0]
            uid_dict_tmp = {}
            m1 = re.findall(r'\/u\\/([\d]+)\?', str2)
            if m1:
                for i in m1:
                    uid_dict_tmp[i] = 1

            self.uid_tmp_list = uid_dict_tmp.keys()
            # print self.uid_tmp_list
            self.insert_uid()
            self.uid_tmp_list = []

            time_now = time.strftime('%Y-%m-%d %X', time.gmtime(time.time()))
            run_page_str = time_now + '---' + response.url + "\r\n"
            with open('run_page', 'ab') as f:
                f.write(run_page_str)

        self.next_page = self.next_page-1
        if self.next_page<1:
            self.next_page = self.largest_page
            # common.stay_cookie(self.name, response.request.headers.getlist('Cookie')[0])
            common.rest(self.spider_sep_per_time)


        next_url = 'http://weibo.com/p/1005052714280233/myfollow?cfs=600&relate=fans&t=1&f=1&type=&Pl_Official_RelationFans__93_page='+str(self.next_page)+'#Pl_Official_RelationFans__93'
        # print 'next_url'
        # print self.next_page
        time.sleep(2.3)
        return [scrapy.Request(url=next_url, meta={'cookiejar': 0}, cookies=self.my_cookies, dont_filter=True, callback=self.see_list
                           )]



    def insert_uid(self):
        if not self.uid_tmp_list:
            return
        t_tuple = []
        for i in self.uid_tmp_list:
            i = int(i)
            # print i
            # t_tuple_tmp = tuple([i])
            # t_tuple.append(t_tuple_tmp)

            sql = "insert into weibo_fensi_info ( `appid`, `uid`  ) values ( %d ,%d)" % (self.appid, i)
            ret = self.mysql_con.excute(sql , "one")

            # print ret







