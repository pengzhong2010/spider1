# -*- coding:utf-8 -*-
import scrapy
# from scrapy.selector import HtmlXPathSelector
from scrapy.selector import Selector
from scrapy.http import HtmlResponse
import re
import time

from rec_driver import *
# from pyredis import RedisKv

from pymysql import PyMysql


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

    mysql_con = ''
    #
    # def parse(self, response):
    #     print 'body'
    #     print response.body
    #     print 'headers'
    #     print response.headers
    #     print 'meta'
    #     print response.meta
    my_headers={
        'Accept': '*/*',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8',

        'Connection':'keep-alive',
        'Host':'passport.weibo.cn',

        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.108 Safari/537.36 2345Explorer/7.1.0.12633',
    }
    def start_requests(self):

        # self.mysql_con = PyMysql(conf1.MYSQL_URL, conf1.MYSQL_PORT, conf1.MYSQL_USER, conf1.MYSQL_PASSWD,
        #                          conf1.MYSQL_DG_DB)



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
        # print response.meta
        # print response.meta['cookiejar']
        # return

        next_url = response.xpath('//a[contains(@class,"btn btnWhite")]//@href').extract()
        # print 'next_url'
        # print next_url[0]

        # print
        time.sleep(1)
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
        # return
        time.sleep(1)
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
        # list_all=self.get_uid_list()

        print 'url'
        print response.url
        print 'body'
        print response.body
        print 'headers'
        print response.headers
        print 'meta'
        print response.meta
        # with open('detail_log_in', 'wb') as f:
        #     f.write(response.body)
        # return
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

                    self.uid_info['info2'] = str2
                    #update db
                    self.update_uid_data()

                    # str2_tmp=str2 + "\r\n"
                    # with open('info2log', 'ab') as f:
                    #     f.write(str2_tmp)

                # self.uid_catching=0
                # time.sleep(10)




        if not self.uid_catching:
            self.uid_info={}

            # self.list_all = self.get_uid_list()
            # self.list_len = len(self.list_all)
            #
            # key_tmp=self.listkey
            # if key_tmp<self.list_len:
            #
            #     uid_tmp=self.list_all[key_tmp]
            # else:
            #     uid_tmp=0
            # self.listkey=self.listkey+1
            self.get_uid_list()
            # print "uid_tmp"
            # print uid_tmp
            # return
            if self.uid_info:
                print self.uid_info
                # return

                uid_tmp=self.uid_info.get("uid")
                if uid_tmp:

                    search_url_tmp=self.uid_search_home_url+str(uid_tmp)
                    return [scrapy.Request(url=search_url_tmp, meta={'cookiejar': response.meta['cookiejar']},
                                           callback=self.uid_home
                                           )]
                else:
                    return self.after_login()


    def uid_home(self,response):

        # print 'url'
        # print response.url
        # print 'body'
        # print response.body
        # print 'headers'
        # print response.headers
        # print 'meta'
        # print response.meta
        # return

        uid_detail_str1=response.body
        uid_detail_str1=str(response.body)

        m1 = re.match(r'.*window\.\$render_data = (.*});.*', uid_detail_str1)
        if m1:
            str1 = m1.groups()[0]
            str2 = str1.replace("\'", '\"')
            # with open('uid_home3', 'ab') as f:
            #     f.write(str2)
            self.uid_info['info1']=str2

        if self.uid_info.get("uid"):
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
        # list1=[1715524730]
        # return list1
        self.uid_info={'id':1,'uid':1715524730}
        return

        if self.list_all:

        # self.list_all = self.get_uid_list()
        # self.list_len = len(self.list_all)

            key_tmp = self.listkey
            if key_tmp < self.list_len:

                uid_dict_tmp = self.list_all[key_tmp]
                self.listkey = self.listkey + 1
                self.uid_info=uid_dict_tmp
                # return uid_tmp
                return

            else:
                self.list_all=self.select_uid_list()
                if self.list_all:
                    self.list_len = len(self.list_all)
                    self.listkey=0
                    return self.get_uid_list()
                else:
                    return
        else:
            self.list_all = self.select_uid_list()
            if self.list_all:
                self.list_len = len(self.list_all)
                self.listkey = 0
                return self.get_uid_list()




    def select_uid_list(self):

        #select uid from weibo_fans_origin where status=0 order by id limit 100

        sql = """
        select id,uid from weibo_fensi_info
            where create_time = 0
            order by id
            limit 100
        """
        ret = self.mysql_con.select(sql)

        if ret:
            res_list_tmp=[]
            for i in ret:
                uid_list_tmp={}
                uid_list_tmp["id"]=i.get("id")
                uid_list_tmp["uid"] = i.get("uid")
                # uid_list_tmp["catch_status"] = i.get("catch_status")
                # uid_tmp = i.get("uid")

                if uid_list_tmp.get("id"):
                    uid_list_tmp["id"] = int(uid_list_tmp["id"])
                    uid_list_tmp["uid"] = int(uid_list_tmp["uid"])

                    res_list_tmp.append(uid_list_tmp)

            return res_list_tmp
        else:


            #loop

            time.sleep(10)
            return self.select_uid_list()
            # return

    def update_uid_data(self):
        data_update=self.uid_info
        if data_update.get("id"):
            print data_update
            with open('info2_171', 'wb') as f:
                f.write(data_update.get("info2"))
            with open('info1_171', 'wb') as f:
                f.write(data_update.get("info1"))












            # if data_update.get("uid"):
            #     sql = "select id from weibo_fensi_info_id where id = %s " % 1237
            #     ret = self.mysql_con.select(sql, 'one')
            #     if ret:
            #         t_tuple = tuple([data_update.get("info1"), data_update.get("info2"), data_update.get("id")])
            #         sql = """
            #                     update weibo_fensi_info_id set info1= %s ,info2= %s ,`catch_status`=1 where id= %s
            #
            #                 """
            #         ret = self.mysql_con.excute(sql, "one", t_tuple)
            #     else:
            #         t_tuple = tuple([data_update.get("id"), data_update.get("info1"), data_update.get("info2")])
            #         sql = """
            #                     insert into weibo_fensi_info_id (id,info1,info2,catch_status) values(%s,%s,%s,1)
            #
            #                 """
            #         ret = self.mysql_con.excute(sql, "one", t_tuple)
            #
            #
            #
            #     t_tuple = tuple([ data_update.get("info1"), data_update.get("info2"), data_update.get("uid")])
            #     sql = """
            #             update weibo_fensi_info_id set info1= %s ,info2= %s ,`status`=1 where uid= %s
            #
            #         """
            #     ret = self.mysql_con.excute(sql, "one", t_tuple)

        return







