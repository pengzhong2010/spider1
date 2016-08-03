# -*- coding:utf-8 -*-
import scrapy
# from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import re
import datetime
import time

from rec_driver import *
# from pyredis import RedisKv

from pymysql import PyMysql


class DetailcatchSpider(scrapy.spiders.Spider):
    name = "detailcatch"
    allowed_domains = ['weibo.com','weibo.cn','sina.com.cn']
    # start_urls=['http://m.weibo.cn']
    surl = 'http://weibo.com'
    # surl = 'http://weibo.com/p/1005051715524730/info?mod=pedit_more'



    # uid_list_tmp=[]
    # uid_list_len=0
    # uid_listkey=0
    uid_info={}
    id_tmp=0
    detail_catching = 0
    mysql_con = ''
    my_cookies={}


    def start_requests(self):
        cookies_list = conf1.MY_COOKIES.split('; ')

        for i in cookies_list:
            tmp = i.split('=')
            k = tmp[0]
            v = tmp[1]
            self.my_cookies.setdefault(k, v)

        self.mysql_con = PyMysql(conf1.MYSQL_URL, conf1.MYSQL_PORT, conf1.MYSQL_USER, conf1.MYSQL_PASSWD,
                                 conf1.MYSQL_DG_DB)

        return [scrapy.Request(url=self.surl, meta={'cookiejar': 0}, cookies=self.my_cookies,  callback=self.see_home
                               )]

    def see_home(self, response):

        # print 'url'
        # print response.url
        # print 'body'
        # print response.body
        # return
        # print 'headers'
        # print response.headers
        # print 'meta'
        # print response.meta
        # print response.meta['cookiejar']

        if self.detail_catching:

            str1=response.body
            str1=str1.replace("\r\n","")
            str1 = str1.replace('\\r\\n', "")
            str1 = str1.replace("\n", "")
            str1 = str1.replace('\\n', "")
            str1=str1.replace("\t","")
            str1 = str1.replace('\\t', "")
            str1 = str1.replace('\\', "")
            m1 = re.match(r'.*\<div id=\"plc_main\"\>\<\/div\>\<\/div\>\"\}\)\<\/script\>(.*)', str1)

            #loop open
            self.detail_catching = 0

            if m1:
                str2= m1.groups()[0]

                self.detail_insert(str2)



            else:
                time_now = time.strftime('%Y-%m-%d %X', time.gmtime(time.time()))
                run_error_str = time_now + '---' + response.url + "---" + "out 2" + "\r\n"
                #/login.sina.com.cn/sso/login.php
                m_url = re.match(r'.*(https://passport.weibo.com/visitor/visitor).*', response.url)
                if m_url:
                    str4 = m_url.groups()[0]
                    run_error_str = run_error_str + "---" + str4
                    with open('run_page_error', 'ab') as f:
                        f.write(run_error_str)
                    return

                m_url1 = re.match(r'.*(login.sina.com.cn/sso/login.php).*', response.url)
                if m_url1:
                    str5 = m_url1.groups()[0]
                    run_error_str = run_error_str + "---" + str5
                    with open('run_page_error', 'ab') as f:
                        f.write(run_error_str)
                    return

                m_url2 = re.match(r'.*(weibo.com/login).*', response.url)
                if m_url2:
                    str6 = m_url2.groups()[0]
                    run_error_str = run_error_str + "---" + str6
                    with open('run_page_error', 'ab') as f:
                        f.write(run_error_str)
                    return
                #login.sina.com.cn
                m_url3 = re.match(r'.*(login.sina.com.cn).*', response.url)
                if m_url3:
                    str7 = m_url3.groups()[0]
                    run_error_str = run_error_str + "---" + str7
                    with open('run_page_error', 'ab') as f:
                        f.write(run_error_str)
                    return

                self.detail_insert('')
                time.sleep(0.3)


                # self.uid_listkey = self.uid_listkey + 1
                # return [
                #     scrapy.Request(url=response.url, meta={'cookiejar': 0}, dont_filter=True, callback=self.see_home
                #                    )]

        if not self.detail_catching:
            time.sleep(0.3)
            self.get_uid_info()
            if self.uid_info.get('uid'):
                print self.uid_info.get('uid')
                # url_tmp='http://weibo.com/'+str(self.uid_info.get('uid'))+'/profile?topnav=1&wvr=6&is_all=1'
                url_tmp='http://weibo.com/p/100505'+str(self.uid_info.get('uid'))+'/info?mod=pedit_more'
                # print url_tmp
                # return
                self.detail_catching=1
                return [
                    scrapy.Request(url=url_tmp, meta={'cookiejar': 0}, dont_filter=True, callback=self.see_home
                                   )]


        return

    def detail_insert(self,text_info):

        id = self.uid_info.get("id")
        time_int = time.mktime(datetime.datetime.now().timetuple())
        time_int = int(time_int)
        t_tuple1 = tuple([time_int, id])

        if not text_info:
            sql = """
                    update weibo_fensi_info set create_time=%s where id=%s

                """
            ret = self.mysql_con.excute(sql, "one", t_tuple1)
            return



        if not id:
            print 'id none'
            return

        t_tuple = tuple([id,text_info])

        sql = """
                insert into weibo_text (
                    id,
                    detail
                ) values (%s,%s)
                on duplicate key update
                    detail = values(detail)

            """
        ret = self.mysql_con.excute(sql, "one", t_tuple)


        if ret:
            sql = """
                    update weibo_fensi_info set create_time=%s where id=%s

                """
            ret = self.mysql_con.excute(sql, "one", t_tuple1)
            w_str=str(id)+"\r\n"
            with open('uid_detail_run', 'ab') as f:
                f.write(w_str)




    def get_uid_info(self):

        # if self.uid_list_tmp:
        #
        #     # self.list_all = self.get_uid_list()
        #     # self.list_len = len(self.list_all)
        #
        #     key_tmp = self.uid_listkey
        #     if key_tmp < self.uid_list_len:
        #
        #         uid_dict_tmp = self.uid_list_tmp[key_tmp]
        #         self.uid_listkey = self.uid_listkey + 1
        #         self.uid_info = uid_dict_tmp
        #         # return uid_tmp
        #         return
        #
        #     else:
        #         self.uid_list_tmp = self.select_uid_info()
        #         if self.uid_list_tmp:
        #             self.uid_list_len = len(self.uid_list_tmp)
        #             self.uid_listkey = 0
        #             return self.get_uid_info()
        #         else:
        #             return
        # else:
        #     self.uid_list_tmp = self.select_uid_info()
        #     if self.uid_list_tmp:
        #         self.uid_list_len = len(self.uid_list_tmp)
        #         self.uid_listkey = 0
        #         return self.get_uid_info()

        self.uid_info = {}
        self.uid_info = self.select_uid_info()
        self.id_tmp = self.uid_info.get('id')

        # self.uid_info = {'id':318,'uid':5643704257}


    def select_uid_info(self):
        # sql = """
        #     select id,uid from weibo_fensi_info
        #         where create_time = 0
        #         order by id
        #         limit 1
        #     """
        # ret = self.mysql_con.select(sql)
        # if ret:
            # res_list_tmp = []
            # for i in ret:
            #     uid_list_tmp = {}
            #     uid_list_tmp["id"] = i.get("id")
            #     uid_list_tmp["uid"] = i.get("uid")
            #     # uid_list_tmp["catch_status"] = i.get("catch_status")
            #     # uid_tmp = i.get("uid")
            #
            #     if uid_list_tmp.get("id"):
            #         uid_list_tmp["id"] = int(uid_list_tmp["id"])
            #         uid_list_tmp["uid"] = int(uid_list_tmp["uid"])
            #
            #         res_list_tmp.append(uid_list_tmp)
            #
            # return res_list_tmp
        # else:
        #
        #     # loop
        #
        #     time.sleep(60)
        #     return self.select_uid_info()

        if not self.id_tmp:
            sql = """
                select id,uid from weibo_fensi_info
                    where create_time = 0
                    order by id
                    limit 1
                """
        else:

            sql = "select id,uid from weibo_fensi_info where create_time = 0 and id > %d order by id limit 1 " % int(
                self.id_tmp)
        ret = self.mysql_con.select(sql)

        if ret:
            uid_list_tmp = {}
            for i in ret:
                uid_list_tmp['id'] = i.get("id")
                uid_list_tmp['uid'] = i.get("uid")

            return uid_list_tmp
        else:
            time.sleep(60)
            return self.select_uid_info()
