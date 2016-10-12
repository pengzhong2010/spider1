# -*- coding:utf-8 -*-
import scrapy
from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
# from scrapy.http import HtmlResponse
import re
import time
import json

from rec_driver import *
# from pyredis import RedisKv

from pymysql import PyMysql


# surl
# start_search_page,end_search_page
# url_fans
# my_cookies

class LeaderboardSpider(scrapy.spiders.Spider):
    name = "leaderboard"
    allowed_domains = ['weibo.com', 'weibo.cn', 'sina.com.cn']
    # start_urls=['http://m.weibo.cn']
    surl = 'http://weibo.com/xiaopapi/profile?rightmod=1&wvr=6&mod=personnumber&is_all=1'

    spider_sep_per_time = 86400
    blog_list=''
    blog_list_key=0
    blog_list_len = 0
    blog_id = 0

    mysql_con = ''
    my_cookies = {}
    error_file_dir = "./error"
    error_file='leaderboard_error'
    appid = 1287792

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
        # with open('commentpage', 'wb') as f:
        #     f.write(response.body)

        #login 过滤
        if not self.login_filter(response.url):
            return


        #db list one
        blog_dict = self.get_blog_one(response.request.headers.getlist('Cookie')[0])
        if not blog_dict:
            return
        #catch
        # self.url_page_demo = 'http://weibo.com/aj/v6/comment/big?ajwvr=6&id='+str(blog_dict['blog_id'])+'&page='

        # next_url='http://weibo.com'+str(blog_dict['url'])
        self.blog_id = blog_dict['blog_id']
        # self.comment_page = 1
        # next_url = self.url_page_demo + str(self.comment_page)
        next_url = 'http://weibo.com' + str(blog_dict['url'])

        return [
            scrapy.Request(url=next_url, meta={'cookiejar': 0}, cookies=self.my_cookies, dont_filter=True, callback=self.page_parse
                           )]


        #prase
        #file write
        #sleep

    def page_parse(self, response):

        if not self.login_filter(response.url):
            return

        # print 'url'
        # print response.url
        # print 'body'
        # print response.body
        # print 'headers'
        # print response.headers
        # print 'meta'
        # print response.meta



        # with open('leaderbd', 'wb') as f:
        #     f.write(response.body)
        # return

        time_now = int(time.time())
        day_now = time.strftime('%Y-%m-%d', time.localtime(time_now))
        day_int_now = int(time.mktime(time.strptime(day_now, '%Y-%m-%d')))

        str1 = response.body
        str1 = str1.replace('\r\n', '')
        str1 = str1.replace('\t', '')
        str1 = str1.replace('\\r\\n', '')
        str1 = str1.replace('\\n', '')
        str1 = str1.replace('\\t', '')
        list1 = Selector(text=str1).xpath('//script/text()').extract()
        for str_html in list1:
            tag = 'FM.view({"ns":"pl.content.weiboDetail.index","domid":"Pl_Official_WeiboDetail__77"'
            m4 = re.match(
                r'.*FM.view\(\{\"ns\":\"pl\.content\.weiboDetail\.index\",\"domid\":\"Pl_Official_WeiboDetail__77\"(.*)',
                str_html)
            if m4:
                m2 = re.match(r'.*\"html\":\"(.*)', str_html)
                if m2:
                    str2 = m2.groups()[0]
                    str2 = str2.replace('\\', '')

                    list3 = Selector(text=str2).xpath(
                        '//ul[contains(@class, "WB_row_line WB_row_r4 clearfix S_line2")]')
                    if list3:
                        list4 = list3[0].xpath('li')
                        if len(list4) == 4:
                            fl_forward_num = 0
                            list5 = list4[1].xpath(
                                '//a[contains(@action-type, "fl_forward")]/span[contains(@class, "pos")]/span[contains(@class, "line S_line1")]/span/em')
                            if len(list5) == 2:
                                fl_forward = list5[1]
                                fl_forward_text = fl_forward.xpath('text()').extract()
                                if fl_forward_text:
                                    fl_forward_num = int(fl_forward_text[0])

                            fl_comment_num = 0
                            list6 = list4[2].xpath(
                                '//a[contains(@action-type, "fl_comment")]/span[contains(@class, "pos")]/span[contains(@class, "line S_line1")]/span/em')
                            if len(list6) == 2:
                                fl_comment = list6[1]
                                fl_comment_text = fl_comment.xpath('text()').extract()
                                if fl_comment_text:
                                    fl_comment_num = int(fl_comment_text[0])

                            fl_like_num = 0
                            list7 = list4[3].xpath(
                                '//a[contains(@action-type, "login")]/span[contains(@class, "pos")]/span[contains(@class, "line S_line1")]')
                            if len(list7) == 2:
                                fl_like_list = list7[1].xpath('span/em')
                                if len(fl_like_list) == 2:
                                    fl_like_text = fl_like_list[1].xpath('text()').extract()
                                if fl_like_text:
                                    fl_like_num = int(fl_like_text[0])

                            # print self.blog_id
                            # print fl_forward_num
                            # print fl_comment_num
                            # print fl_like_num
                            # print day_int_now

                            self.update_blog_info(self.blog_id, fl_forward_num, fl_comment_num, fl_like_num, day_int_now)
        # return



        # db list one
        blog_dict = self.get_blog_one(response.request.headers.getlist('Cookie')[0])
        if not blog_dict:
            return
        # catch
        # self.url_page_demo = 'http://weibo.com/aj/v6/comment/big?ajwvr=6&id='+str(blog_dict['blog_id'])+'&page='

        # next_url='http://weibo.com'+str(blog_dict['url'])
        self.blog_id = blog_dict['blog_id']
        # self.comment_page = 1
        # next_url = self.url_page_demo + str(self.comment_page)
        next_url = 'http://weibo.com' + str(blog_dict['url'])

        return [
            scrapy.Request(url=next_url, meta={'cookiejar': 0}, cookies=self.my_cookies, dont_filter=True,
                           callback=self.page_parse
                           )]



    def login_filter(self,url):
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

    def get_blog_one(self,cookies_str):
        dict_tmp = {}
        if not self.blog_list:
            self.get_blog_list()

        if self.blog_list:
            if self.blog_list_key<self.blog_list_len:
                dict_tmp = self.blog_list[self.blog_list_key]
                self.blog_list_key = self.blog_list_key + 1
            else:
                self.blog_list=''
                self.blog_list_len = 0
                self.blog_list_key = 0
                #sleep
                self.stay_cookie(cookies_str)
                self.rest()
                return self.get_blog_one(cookies_str)
                pass
        return dict_tmp
    def get_blog_list(self):
        sql = " select * from weibo_blog where appid = "+str(self.appid)+" order by create_time desc limit 20"
        ret = self.mysql_con.select(sql)
        if ret:
            self.blog_list = ret
            self.blog_list_len=len(ret)


    def rest(self):
        time.sleep(self.spider_sep_per_time)

    # def output_comment(self, blog_id, comment_id, comment_user_id, comment_text, datatime, comment_user_nickname):
    #     date_now = time.strftime('%Y-%m-%d', time.gmtime(time.time()))
    #     file_dir = "./comment_data"
    #     if not os.path.exists(file_dir):
    #         os.makedirs(file_dir)
    #     if not os.path.exists(file_dir+'/'+str(self.appid)):
    #         os.makedirs(file_dir+'/'+str(self.appid))
    #
    #     str1 = str(blog_id) +"\t"+ comment_id +"\t"+ comment_user_id +"\t"+ comment_text +"\t"+ str(datatime) +"\t"+ comment_user_nickname + "\r\n"
    #     with open(file_dir+'/'+str(self.appid)+'/'+str(blog_id), 'ab') as f:
    #         f.write(str1)

    def update_blog_info(self, blog_id, fl_forward_num, fl_comment_num, fl_like_num, day_int_now):

        t_tuple = tuple([fl_forward_num, fl_comment_num, fl_like_num, day_int_now, blog_id])

        sql = "update weibo_blog set forward_count = %s , comment_count = %s , dianzan_count = %s , last_update_time = %s where blog_id = %s"
        # print sql
        ret = self.mysql_con.excute(sql, "one", t_tuple)

        # print ret

    def stay_cookie(self, cookies_str):
        file_dir = "./tmp"
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)

        with open(file_dir + '/' + str(self.name) + '_cookies', 'wb') as f:
            f.write(cookies_str)

    def read_cookie(self):
        file_dir = "./tmp"
        cookies_file_name = 'commentlist'
        if os.path.exists(file_dir + '/' + cookies_file_name + '_cookies'):
            f = open(file_dir + '/' + cookies_file_name + '_cookies')
            cookies_str = f.read()
            if cookies_str:
                return cookies_str

        if os.path.exists(file_dir + '/' + str(self.name) + '_cookies'):
            f = open(file_dir + '/' + str(self.name) + '_cookies')
            cookies_str = f.read()
            if cookies_str:
                return cookies_str
        return conf1.MY_COOKIES




