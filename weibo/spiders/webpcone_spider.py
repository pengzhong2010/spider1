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


# surl
# start_search_page,end_search_page
# url_fans
# my_cookies

class WebpconeSpider(scrapy.spiders.Spider):
    name = "webpcone"
    allowed_domains = ['weibo.com', 'weibo.cn', 'sina.com.cn']
    # start_urls=['http://m.weibo.cn']
    spider_sep_per_time = 1500

    surl = 'http://weibo.com/2714280233/follow?from=page_100505&wvr=6&mod=headfollow#place'
    page_search_url = ''
    start_page = 1
    run_page = 0
    start_search_page = 0
    end_search_page = 51
    login_uid = 0
    uid_tmp_list = []
    uid_write_num = 99
    uid_num_tmp = 0
    uid_str_tmp = ''
    write_num = 99
    num_tmp = 0
    str_tmp = ''
    uid_filename = 'uid186'
    resjson_filename = 'weibo186'
    resjson_error_filename = 'error186'
    next_page=50

    mysql_con = ''
    error_file_dir = "./error"
    error_file = 'fanslist_error'

    my_headers = {}
    my_cookies = {}

    def start_requests(self):

        cookies_list = self.read_cookie().split('; ')

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

        if not self.login_filter(response.url):
            return

        # response.xpath('')
        url_tmp = response.url
        url_tmp = str(url_tmp)
        m1 = re.match(r'.*\/(\d+)\/.*', url_tmp)
        if m1:
            self.login_uid = m1.groups()[0]

            # url_fans='http://weibo.com/' + str(self.login_uid) + '/fans?rightmod=1&wvr=6'
            url_fans = 'http://weibo.com/2714280233/fans?cfs=600&relate=fans&t=1&f=1&type=&Pl_Official_RelationFans__103_page=50#Pl_Official_RelationFans__103'
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

        if not self.login_filter(response.url):
            return

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
            self.next_page = 50
            self.stay_cookie(response.request.headers.getlist('Cookie')[0])
            self.rest()


        next_url = 'http://weibo.com/p/1005052714280233/myfollow?cfs=600&relate=fans&t=1&f=1&type=&Pl_Official_RelationFans__93_page='+str(self.next_page)+'#Pl_Official_RelationFans__93'
        # print 'next_url'
        # print self.next_page
        time.sleep(2.3)
        return [scrapy.Request(url=next_url, meta={'cookiejar': 0}, cookies=self.my_cookies, dont_filter=True, callback=self.see_list
                           )]




    def see_other_list(self, response):

        pass

    def insert_uid(self):
        if not self.uid_tmp_list:
            return
        t_tuple = []
        for i in self.uid_tmp_list:
            i = int(i)
            # t_tuple_tmp = tuple([i])
            # t_tuple.append(t_tuple_tmp)

            sql = "insert into weibo_fensi_info ( `uid` ) values ( %d )" % i
            ret = self.mysql_con.excute(sql , "one")

            # print ret

    def login_filter(self, url):
        if not os.path.exists(self.error_file_dir):
            os.makedirs(self.error_file_dir)
        time_now = time.strftime('%Y-%m-%d %X', time.gmtime(time.time()))
        run_error_str = time_now + '---' + url + "---" + "login faild" + "\r\n"
        m_url = re.match(r'.*(https://passport.weibo.com/visitor/visitor).*', url)
        if m_url:
            str4 = m_url.groups()[0]
            run_error_str = run_error_str + "---" + str4
            with open(self.error_file_dir + '/' + self.error_file, 'ab') as f:
                f.write(run_error_str)
            return

        m_url1 = re.match(r'.*(login.sina.com.cn/sso/login.php).*', url)
        if m_url1:
            str5 = m_url1.groups()[0]
            run_error_str = run_error_str + "---" + str5
            with open(self.error_file_dir + '/' + self.error_file, 'ab') as f:
                f.write(run_error_str)
            return

        m_url2 = re.match(r'.*(weibo.com/login).*', url)
        if m_url2:
            str6 = m_url2.groups()[0]
            run_error_str = run_error_str + "---" + str6
            with open(self.error_file_dir + '/' + self.error_file, 'ab') as f:
                f.write(run_error_str)
            return
        # login.sina.com.cn
        m_url3 = re.match(r'.*(login.sina.com.cn).*', url)
        if m_url3:
            str7 = m_url3.groups()[0]
            run_error_str = run_error_str + "---" + str7
            with open(self.error_file_dir + '/' + self.error_file, 'ab') as f:
                f.write(run_error_str)
            return
        return True

    def rest(self):
        time.sleep(self.spider_sep_per_time)

    def stay_cookie(self, cookies_str):
        file_dir = "./tmp"
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

        with open(file_dir + '/' + str(self.name) + '_cookies', 'wb') as f:
            f.write(cookies_str)

    def read_cookie(self):
        file_dir = "./tmp"
        if os.path.exists(file_dir + '/' + str(self.name) + '_cookies'):
            f = open(file_dir + '/' + str(self.name) + '_cookies')
            cookies_str = f.read()
            if cookies_str:
                return cookies_str
        return conf1.PAPI_COOKIES

