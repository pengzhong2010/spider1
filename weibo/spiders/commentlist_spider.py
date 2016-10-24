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

class CommentlistSpider(scrapy.spiders.Spider):
    name = "commentlist"
    allowed_domains = ['weibo.com', 'weibo.cn', 'sina.com.cn']
    # start_urls=['http://m.weibo.cn']
    surl='http://weibo.com/xiaopapi/profile?rightmod=1&wvr=6&mod=personnumber&is_all=1'

    spider_sep_per_time=3600

    mysql_con = ''

    my_cookies = {}
    error_file_dir = "./error"
    error_file = 'commentlist_error'
    appid=1287792

    def start_requests(self):
        cookies_list = self.read_cookie().split('; ')
        for i in cookies_list:
            tmp = i.split('=')

            k = tmp[0]

            v = tmp[1]

            self.my_cookies.setdefault(k, v)

        self.mysql_con = PyMysql(conf1.MYSQL_URL, conf1.MYSQL_PORT, conf1.MYSQL_USER, conf1.MYSQL_PASSWD,
                                 conf1.MYSQL_DG_DB)
        # print self.my_cookies
        return [scrapy.Request(url=self.surl, meta={'cookiejar': 0}, cookies=self.my_cookies, callback=self.see_list
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
        # print 'cookies'
        # print type(response.request.headers.getlist('Cookie')[0])
        # print response.request.headers.getlist('Cookie')[0]
        # return

        if not self.login_filter(response.url):
            return


        # with open('commentlist1', 'wb') as f:
        #     f.write(response.body)
        # return

        str1 = response.body
        str1 = str1.replace('\r\n', '')
        str1 = str1.replace('\t', '')
        str1 = str1.replace('\\r\\n', '')
        str1 = str1.replace('\\n', '')
        str1 = str1.replace('\\t', '')
        list1 = Selector(text=str1).xpath('//script/text()').extract()
        blog_list = []
        for str_html in list1:
            tag = 'FM.view({"ns":"pl.content.homeFeed.index","domid":"Pl_Official_MyProfileFeed__24"'
            # m4 = re.match(
            #     r'.*FM.view\(\{\"ns\":\"pl\.content\.homeFeed\.index\",\"domid\":\"Pl_Official_MyProfileFeed__24\"(.*)',
            #     str_html)
            m4 = re.match(
                r'.*FM.view\(\{\"ns\":\"pl\.content\.homeFeed\.index\",\"domid\":\"Pl_Official_MyProfileFeed__36\"(.*)',
                str_html)
            if m4:
                m2 = re.match(r'.*\"html\":\"(.*)', str_html)
                if m2:
                    str2 = m2.groups()[0]
                    str2 = str2.replace('\\', '')
                    list3 = Selector(text=str2).xpath('//div[contains(@class, "WB_detail")]')
                    # blog_list=[]
                    for index1, link1 in enumerate(list3):
                        name_tmp = ''
                        href_tmp = ''
                        date_tmp = ''
                        title_tmp = ''
                        list2 = link1.xpath('div[contains(@class, "WB_from S_txt2")]')
                        for index, link in enumerate(list2):

                            list_tmp = link.xpath('a')
                            if not list_tmp:
                                continue
                            # print list_tmp.extract()
                            name_list_tmp = list_tmp.xpath('@name').extract()
                            if not name_list_tmp:
                                continue
                            name_tmp = str(name_list_tmp[0])
                            href_list_tmp = list_tmp.xpath('@href').extract()
                            if href_list_tmp:
                                href_tmp = str(href_list_tmp[0])
                            date_list_tmp = list_tmp.xpath('@date').extract()
                            if date_list_tmp:
                                date_tmp = str(date_list_tmp[0])
                            date_tmp = date_tmp[0:10]
                            # print name_tmp
                            # print href_tmp
                            # print date_tmp
                        list_title = link1.xpath('div[contains(@class, "WB_text W_f14")]/text()').extract()
                        # print list_title
                        if list_title:
                            for i in list_title:
                                i = i.strip()
                                if i:
                                    title_tmp = i
                                    # gbkTypeStr = title_tmp.encode("GBK", 'ignore')
                                    # print gbkTypeStr
                                    break

                        blog_dict = {}
                        blog_dict['blog_id'] = name_tmp
                        blog_dict['url'] = href_tmp
                        blog_dict['create_time'] = date_tmp
                        blog_dict['title'] = title_tmp
                        blog_list.append(blog_dict)
                        # print blog_dict
                    # print blog_list

                    self.check_blog(blog_list)

            m4 = re.match(
                r'.*FM.view\(\{\"ns\":\"pl\.content\.homeFeed\.index\",\"domid\":\"Pl_Official_MyProfileFeed__22\"(.*)',
                str_html)
            if m4:
                m2 = re.match(r'.*\"html\":\"(.*)', str_html)
                if m2:
                    str2 = m2.groups()[0]
                    str2 = str2.replace('\\', '')
                    list3 = Selector(text=str2).xpath('//div[contains(@class, "WB_detail")]')
                    # blog_list=[]
                    for index1, link1 in enumerate(list3):
                        name_tmp = ''
                        href_tmp = ''
                        date_tmp = ''
                        title_tmp = ''
                        list2 = link1.xpath('div[contains(@class, "WB_from S_txt2")]')
                        for index, link in enumerate(list2):

                            list_tmp = link.xpath('a')
                            if not list_tmp:
                                continue
                            # print list_tmp.extract()
                            name_list_tmp = list_tmp.xpath('@name').extract()
                            if not name_list_tmp:
                                continue
                            name_tmp = str(name_list_tmp[0])
                            href_list_tmp = list_tmp.xpath('@href').extract()
                            if href_list_tmp:
                                href_tmp = str(href_list_tmp[0])
                            date_list_tmp = list_tmp.xpath('@date').extract()
                            if date_list_tmp:
                                date_tmp = str(date_list_tmp[0])
                            date_tmp = date_tmp[0:10]
                            # print name_tmp
                            # print href_tmp
                            # print date_tmp
                        list_title = link1.xpath('div[contains(@class, "WB_text W_f14")]/text()').extract()
                        # print list_title
                        if list_title:
                            for i in list_title:
                                i = i.strip()
                                if i:
                                    title_tmp = i
                                    # gbkTypeStr = title_tmp.encode("GBK", 'ignore')
                                    # print gbkTypeStr
                                    break

                        blog_dict = {}
                        blog_dict['blog_id'] = name_tmp
                        blog_dict['url'] = href_tmp
                        blog_dict['create_time'] = date_tmp
                        blog_dict['title'] = title_tmp
                        blog_list.append(blog_dict)

                        # print blog_dict
                    # print blog_list

                    self.check_blog(blog_list)

        if not blog_list:
            self.catch_filter(response.url)

        self.stay_cookie(response.request.headers.getlist('Cookie')[0])
        self.rest()
        return [
            scrapy.Request(url=self.surl, meta={'cookiejar': 0}, cookies=self.my_cookies, dont_filter=True, callback=self.see_list
                           )]



    def check_blog(self,list):
        if not list:
            return
        # print list
        for i in list:
            blog_id=i.get('blog_id')
            if not blog_id:
                continue

            sql = "select blog_id from weibo_blog where blog_id = "+blog_id+"  limit 1 "
            ret = self.mysql_con.select(sql)
            # print ret

            if not ret:
                blog_url=i.get('url')
                blog_create_time=i.get('create_time')
                blog_title=i.get('title')
                b= blog_url and blog_create_time and blog_title
                if b:

                    t_tuple = tuple([blog_id, blog_url, blog_create_time, blog_title, self.appid])

                    sql = """
                                    insert into weibo_blog (
                                        blog_id,
                                        url,
                                        create_time,
                                        title,
                                        appid
                                    ) values (%s,%s,%s,%s,%s)

                                """
                    ret = self.mysql_con.excute(sql, "one", t_tuple)

                    # print ret

    def rest(self):
        time.sleep(self.spider_sep_per_time)

    def login_filter(self, url):
        if not os.path.exists(self.error_file_dir):
            os.makedirs(self.error_file_dir)
        time_now = time.strftime('%Y-%m-%d %X', time.gmtime(time.time()))
        run_error_str = time_now + '---' + url + "---" + "login faild" + "\r\n"
        m_url = re.match(r'.*(https://passport.weibo.com/visitor/visitor).*', url)
        if m_url:
            str4 = m_url.groups()[0]
            run_error_str = run_error_str + "---" + str4
            with open(self.error_file_dir+'/'+self.error_file, 'ab') as f:
                f.write(run_error_str)
            return

        m_url1 = re.match(r'.*(login.sina.com.cn/sso/login.php).*', url)
        if m_url1:
            str5 = m_url1.groups()[0]
            run_error_str = run_error_str + "---" + str5
            with open(self.error_file_dir+'/'+self.error_file, 'ab') as f:
                f.write(run_error_str)
            return

        m_url2 = re.match(r'.*(weibo.com/login).*', url)
        if m_url2:
            str6 = m_url2.groups()[0]
            run_error_str = run_error_str + "---" + str6
            with open(self.error_file_dir+'/'+self.error_file, 'ab') as f:
                f.write(run_error_str)
            return
        # login.sina.com.cn
        m_url3 = re.match(r'.*(login.sina.com.cn).*', url)
        if m_url3:
            str7 = m_url3.groups()[0]
            run_error_str = run_error_str + "---" + str7
            with open(self.error_file_dir+'/'+self.error_file, 'ab') as f:
                f.write(run_error_str)
            return
        return True

    def catch_filter(self, url):
        if not os.path.exists(self.error_file_dir):
            os.makedirs(self.error_file_dir)
        time_now = time.strftime('%Y-%m-%d %X', time.gmtime(time.time()))
        run_error_str = time_now + '---' + url + "---" + "catch faild" + "\r\n"
        str4 = 'catch nothing'
        run_error_str = run_error_str + "---" + str4
        with open(self.error_file_dir + '/' + self.error_file, 'ab') as f:
            f.write(run_error_str)
        return

    def stay_cookie(self,cookies_str):
        file_dir = "./tmp"
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

        with open(file_dir + '/' + str(self.name)+'_cookies', 'wb') as f:
            f.write(cookies_str)

    def read_cookie(self):
        file_dir = "./tmp"
        if os.path.exists(file_dir + '/' + str(self.name)+'_cookies'):
            f = open(file_dir + '/' + str(self.name) + '_cookies')
            cookies_str = f.read()
            if cookies_str:
                return cookies_str
        return conf1.MY_COOKIES
