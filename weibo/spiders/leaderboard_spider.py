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
import common


class LeaderboardSpider(scrapy.spiders.Spider):
    name = "leaderboard"
    allowed_domains = ['weibo.com', 'weibo.cn', 'sina.com.cn']
    # start_urls=['http://m.weibo.cn']
    surl = 'http://weibo.com/xiaopapi/profile?rightmod=1&wvr=6&mod=personnumber&is_all=1'

    spider_sep_per_time = 7200
    blog_list=''
    blog_list_key=0
    blog_list_len = 0
    blog_id = 0

    mysql_con = ''
    my_cookies = {}
    error_file_dir = ""
    error_file=''
    cookies_user = conf1.MY_COOKIES1
    appid = 1287792

    def shell_init(self):
        self.error_file_dir = conf1.error_file_dir
        self.error_file = self.name + '_error'

    def start_requests(self):
        self.shell_init()
        cookies_list = common.read_cookie(self.name, self.cookies_user).split('; ')

        for i in cookies_list:
            tmp = i.split('=')

            k = tmp[0]

            v = tmp[1]

            self.my_cookies.setdefault(k, v)

        self.mysql_con = PyMysql(conf1.MYSQL_URL, conf1.MYSQL_PORT, conf1.MYSQL_USER, conf1.MYSQL_PASSWD,
                                 conf1.MYSQL_DG_DB)
        # self.surl='http://weibo.com/2810373291/EdcVu08Rz?type=comment#_rnd1476759480516'
        return [scrapy.Request(url=self.surl, meta={'cookiejar': 4}, cookies=self.my_cookies, callback=self.see_home
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
        # with open('leaderboard2', 'wb') as f:
        #     f.write(response.body)

        #login 过滤
        if not common.login_filter(self.error_file_dir, self.error_file, response.url):
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
            scrapy.Request(url=next_url, meta={'cookiejar': 4}, cookies=self.my_cookies, dont_filter=True, callback=self.page_parse
                           )]


        #prase
        #file write
        #sleep

    def page_parse(self, response):

        if not common.login_filter(self.error_file_dir, self.error_file, response.url):
            return
        common.stay_cookie(self.name, response.request.headers.getlist('Cookie')[0])

        # print 'url'
        # print response.url
        # print 'body'
        # print response.body
        # print 'headers'
        # print response.headers
        # print 'meta'
        # print response.meta



        # with open('leaderbd1', 'wb') as f:
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
                r'.*FM.view\(\{\"ns\":\"pl\.content\.weiboDetail\.index\",\"domid\":\"Pl_Official_WeiboDetail__75\"(.*)',
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

                            # fl_like_num = 0
                            # list7 = list4[3].xpath(
                            #     '//a[contains(@action-type, "login")]/span[contains(@class, "pos")]/span[contains(@class, "line S_line1")]')
                            # if len(list7) == 2:
                            #     fl_like_list = list7[1].xpath('span/em')
                            #     if len(fl_like_list) == 2:
                            #         fl_like_text = fl_like_list[1].xpath('text()').extract()
                            #     if fl_like_text:
                            #         fl_like_num = int(fl_like_text[0])

                            fl_like_num = 0
                            fl_like_list = list4[3].xpath(
                                '//a[contains(@action-type, "fl_like")]/span[contains(@class, "pos")]/span[contains(@class, "line S_line1")]/span/em')
                            if len(fl_like_list) == 2:
                                fl_like_text = fl_like_list[1].xpath('text()').extract()
                                if fl_like_text:
                                    fl_like_num = int(fl_like_text[0])
                            else:
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

            m4 = re.match(
                r'.*FM.view\(\{\"ns\":\"pl\.content\.weiboDetail\.index\",\"domid\":\"Pl_Official_WeiboDetail__60\"(.*)',
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

                            # fl_like_num = 0
                            # list7 = list4[3].xpath(
                            #     '//a[contains(@action-type, "login")]/span[contains(@class, "pos")]/span[contains(@class, "line S_line1")]')
                            # if len(list7) == 2:
                            #     fl_like_list = list7[1].xpath('span/em')
                            #     if len(fl_like_list) == 2:
                            #         fl_like_text = fl_like_list[1].xpath('text()').extract()
                            #     if fl_like_text:
                            #         fl_like_num = int(fl_like_text[0])

                            fl_like_num = 0
                            fl_like_list = list4[3].xpath(
                                '//a[contains(@action-type, "fl_like")]/span[contains(@class, "pos")]/span[contains(@class, "line S_line1")]/span/em')
                            if len(fl_like_list) == 2:
                                fl_like_text = fl_like_list[1].xpath('text()').extract()
                                if fl_like_text:
                                    fl_like_num = int(fl_like_text[0])
                            else:
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
        time.sleep(3)
        return [
            scrapy.Request(url=next_url, meta={'cookiejar': 4}, cookies=self.my_cookies, dont_filter=True,
                           callback=self.page_parse
                           )]



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
                # self.stay_cookie(cookies_str)
                common.rest(self.spider_sep_per_time)
                return self.get_blog_one(cookies_str)
                pass
        return dict_tmp
    def get_blog_list(self):
        sql = " select * from weibo_blog where appid = "+str(self.appid)+" order by create_time desc limit 20"
        ret = self.mysql_con.select(sql)
        if ret:
            self.blog_list = ret
            self.blog_list_len=len(ret)




    def update_blog_info(self, blog_id, fl_forward_num, fl_comment_num, fl_like_num, day_int_now):

        t_tuple = tuple([fl_forward_num, fl_comment_num, fl_like_num, day_int_now, blog_id])

        sql = "update weibo_blog set forward_count = %s , comment_count = %s , dianzan_count = %s , last_update_time = %s where blog_id = %s"
        # print sql
        ret = self.mysql_con.excute(sql, "one", t_tuple)

        # print ret










