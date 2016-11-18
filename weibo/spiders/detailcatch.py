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
import common


class DetailcatchSpider(scrapy.spiders.Spider):
    name = "detailcatch"
    allowed_domains = ['weibo.com','weibo.cn','sina.com.cn']
    # start_urls=['http://m.weibo.cn']
    # surl = 'http://weibo.com'
    surl = 'http://weibo.com/p/1005051715524730/info?mod=pedit_more'

    spider_sep_per_time = 3600

    uid_info={}
    # id_tmp=0
    detail_catching = 0
    mysql_con = ''
    my_cookies={}

    error_file_dir = ""
    error_file = ''
    cookies_user = conf1.MY_COOKIES
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
        # return
        # print response.meta['cookiejar']

        if not common.login_filter(self.error_file_dir, self.error_file, response.url):
            return
        common.stay_cookie(self.name, response.request.headers.getlist('Cookie')[0])


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
                # with open('u_detail_tmp', 'wb') as f:
                #     f.write(str2)

                if str2:
                    pinfo = self.parse_text(str2)
                    # print pinfo
                    if pinfo:
                        self.fans_info_update(pinfo)
                    else:
                        self.fans_info_update_time()
                else:
                    self.fans_info_update_time()
            else:
                self.fans_info_update_time()
            # return

                # self.detail_insert(str2)



        if not self.detail_catching:
            time.sleep(1.3)
            self.detail_catching = 1
            self.get_uid_info()
            # self.uid_info = {'id': 3203330L, 'uid': 5994845281L}

            if self.uid_info.get('uid'):
                url_tmp='http://weibo.com/p/100505'+str(self.uid_info.get('uid'))+'/info?mod=pedit_more'

                return [
                    scrapy.Request(url=url_tmp, meta={'cookiejar': 0}, cookies=self.my_cookies, dont_filter=True, callback=self.see_home
                                   )]


        return

    # def detail_insert(self,text_info):
    #
    #     id = self.uid_info.get("id")
    #     time_int = time.mktime(datetime.datetime.now().timetuple())
    #     time_int = int(time_int)
    #     t_tuple1 = tuple([time_int, id])
    #
    #     if not text_info:
    #         sql = """
    #                 update weibo_fensi_info set create_time=%s where id=%s
    #
    #             """
    #         ret = self.mysql_con.excute(sql, "one", t_tuple1)
    #         return
    #
    #
    #
    #     if not id:
    #         print 'id none'
    #         return
    #
    #     t_tuple = tuple([id,text_info])
    #
    #     sql = """
    #             insert into weibo_text (
    #                 id,
    #                 detail
    #             ) values (%s,%s)
    #             on duplicate key update
    #                 detail = values(detail)
    #
    #         """
    #     ret = self.mysql_con.excute(sql, "one", t_tuple)
    #
    #
    #     if ret:
    #         sql = """
    #                 update weibo_fensi_info set create_time=%s where id=%s
    #
    #             """
    #         ret = self.mysql_con.excute(sql, "one", t_tuple1)
    #         w_str=str(id)+"\r\n"
    #         with open('uid_detail_run', 'ab') as f:
    #             f.write(w_str)
    #



    def parse_text(self,str1):
        info = {}
        try:
            m2 = re.match(r'.*\"html\":\"\<!--模块--\>(.*)', str1)
            if m2:
                str2 = m2.groups()[0]

                list1 = Selector(text=str2).xpath('//div[contains(@class, "m_wrap clearfix")]/ul/li')
                # print list1
                for index, link in enumerate(list1):
                    key = ''
                    values = []
                    list_tmp = link.xpath('span/text()').extract()
                    if list_tmp:
                        key = list_tmp[0]
                        if key == u'昵称：':
                            info['nick_name'] = list_tmp[1]
                        elif key == u'所在地：':
                            position_list = list_tmp[1].split(' ')
                            position_len = len(position_list)
                            if position_len:
                                info['province'] = position_list[0]
                                if position_len > 1:
                                    info['city'] = position_list[1]
                        elif key == u'性别：':
                            if list_tmp[1] == u'男':
                                info['sex'] = 1
                            else:
                                info['sex'] = 0
                        elif key == u'简介：':
                            info['desc_fill'] = str(list_tmp[1])
                        elif key == u'生日：':
                            str_s = list_tmp[1]
                            try:
                                str_s = str_s.replace(u'年', '-')
                                str_s = str_s.replace(u'月', '-')
                                str_s = str_s.replace(u'日', '')
                                br_list = str_s.split('-')

                                br_m = int(br_list[1])
                                if br_m < 10:
                                    br_m_str = '0' + str(br_m)
                                else:
                                    br_m_str = str(br_m)
                                br_list[1] = br_m_str
                                br_m = int(br_list[2])
                                if br_m < 10:
                                    br_m_str = '0' + str(br_m)
                                else:
                                    br_m_str = str(br_m)
                                br_list[2] = br_m_str
                                str_s = '-'.join(br_list)
                                # print str_s

                                s = time.mktime(time.strptime(str(str_s), '%Y-%m-%d'))
                            except Exception as e:
                                s = 0
                            info['birth_fill'] = int(s)


                        elif key == u'注册时间：':
                            # print list_tmp
                            str_s = list_tmp[1]
                            s = time.mktime(time.strptime(str_s, '%Y-%m-%d'))
                            info['regis_date'] = int(s)
                        elif key == u'公司：':
                            company_list = link.xpath('span')
                            company_list_info = []
                            for ix, linkx in enumerate(company_list):
                                company_one_list = linkx.xpath('text()').extract()
                                company_one_str = ''
                                if not company_one_list[0] == u'公司：':
                                    part1 = linkx.xpath('a/text()').extract()
                                    company_one_str = part1[0]
                                    # print company_one_str
                                    for i in company_one_list:
                                        company_one_str = company_one_str + i
                                    # print company_one_str
                                    company_list_info.append(company_one_str)
                            # info['company'] = json.dumps(company_list_info)
                            info['company'] = ';'.join(company_list_info)
                        elif key == u'大学：':
                            university_list = link.xpath('span')
                            university_list_info = []
                            for ix, linkx in enumerate(university_list):
                                university_one_list = linkx.xpath('text()').extract()
                                university_one_str = ''
                                if not university_one_list[0] == u'大学：':
                                    part1 = linkx.xpath('a/text()').extract()
                                    university_one_str = part1[0]
                                    # print company_one_str
                                    for i in university_one_list:
                                        university_one_str = university_one_str + i
                                    # print university_one_str
                                    university_list_info.append(university_one_str)
                            # info['university'] = json.dumps(university_list_info)
                            info['university'] = ';'.join(university_list_info)
                        elif key == u'标签：':
                            spans = link.xpath('span/a/text()').extract()
                            if spans:
                                info['tags'] = ';'.join(spans)
                                # tags=spans[1]

            # "html":"<div class="PRF_modwrap S_line1 clearfix">
            m3 = re.match(r'.*\"html\":\"\<div class=\"PRF_modwrap S_line1 clearfix\"\>(.*)', str1)
            if m3:
                str3 = m3.groups()[0]
                # print str3
                list2 = Selector(text=str3).xpath('//p[contains(@class, "level_info")]/span')
                # print list2.extract()
                for index, link in enumerate(list2):
                    x1 = link.xpath('text()').extract()
                    x2 = link.xpath('span/text()').extract()

                    # print x1[0]
                    # print x2[0]
                    if x1[0] == u' 当前等级： ':
                        m3_1 = re.match(r'.*([\d]+).*', x2[0])
                        if m3_1:
                            info['weibo_level'] = m3_1.groups()[0]
                            # print m3_1.groups()

                    elif x1[0] == u' 经验值： ':
                        info['exp_value'] = x2[0]


                        # print list2

            # "html":"<div class="WB_cardwrap S_bg2" >
            # print 123123
            #<div class="WB_cardwrap S_bg2" ><div class="PCD_counter">
            m4 = re.match(r'.*\"html\":\"\<div class=\"WB_cardwrap S_bg2\" \>\<div class=\"PCD_counter\"\>(.*)', str1)
            #Pl_Core_T8CustomTriColumn__55
            # print m4.groups()
            if m4:
                str4 = m4.groups()[0]
                list4 = Selector(text=str4).xpath('//table[contains(@class, "tb_counter")]/tbody/tr/td/a')

                for index, link4 in enumerate(list4):

                    x1 = link4.xpath('span/text()').extract()
                    x2 = link4.xpath('strong/text()').extract()
                    # print x1
                    # print x2

                    if x1[0] == u'关注':
                        info['attr_count'] = x2[0]
                    elif x1[0] == u'粉丝':
                        info['fensi_count'] = x2[0]
                    elif x1[0] == u'微博':
                        info['weibo_count'] = x2[0]
            # else:
            #     print "not match"

            # print info
            # self.uid_info = info
        except Exception as e:
            pass

        return info

    def fans_info_update(self, info):
        if not info:
            return
        info_keys = []
        info_values = []

        nick_name = info.get('nick_name')
        if nick_name:
            info_keys.append('nick_name')
            info_values.append(nick_name)
        attr_count = info.get('attr_count')
        if attr_count:
            info_keys.append('attr_count')
            info_values.append(int(attr_count))
        weibo_count = info.get('weibo_count')
        if weibo_count:
            info_keys.append('weibo_count')
            info_values.append(int(weibo_count))
        fensi_count = info.get('fensi_count')
        if fensi_count:
            info_keys.append('fensi_count')
            info_values.append(int(fensi_count))

        weibo_level = info.get('weibo_level')
        if weibo_level:
            info_keys.append('weibo_level')
            info_values.append(int(weibo_level))

        exp_value = info.get('exp_value')
        if exp_value:
            info_keys.append('exp_value')
            info_values.append(int(exp_value))
        sex = info.get('sex')
        if sex is not None:
            info_keys.append('sex')
            info_values.append(sex)
        city = info.get('city')
        if city:
            info_keys.append('city')
            info_values.append(city)
        province = info.get('province')
        if province:
            info_keys.append('province')
            info_values.append(province)
        university = info.get('university')
        if university:
            info_keys.append('university')
            info_values.append(university)
        company = info.get('company')
        if company:
            info_keys.append('company')
            info_values.append(company)
        desc_fill = info.get('desc_fill')
        if desc_fill:
            info_keys.append('desc_fill')
            info_values.append(desc_fill)
        tags = info.get('tags')
        if tags:
            info_keys.append('tags')
            info_values.append(tags)
        birth_fill = info.get('birth_fill')
        if birth_fill:
            info_keys.append('birth_fill')
            info_values.append(birth_fill)
        regis_date = info.get('regis_date')
        if regis_date:
            info_keys.append('regis_date')
            info_values.append(regis_date)

        time_int = time.mktime(datetime.datetime.now().timetuple())
        last_update_time = int(time_int)
        create_time = last_update_time
        info_keys.append('create_time')
        info_values.append(create_time)
        info_keys.append('last_update_time')
        info_values.append(last_update_time)


        t_tuple = tuple(info_values)
        ss = ' = %s , '.join(info_keys)
        id = self.uid_info.get('id')
        if id:
            sql = "update weibo_fensi_info set " + ss + " = %s where id = " + str(id) + " "
            print sql
            print info_values
            ret = self.mysql_con.excute(sql, "one", t_tuple)
            print ret


    def fans_info_update_time(self):
        info_keys = []
        info_values = []
        time_int = time.mktime(datetime.datetime.now().timetuple())
        create_time = int(time_int)
        info_keys.append('create_time')
        info_values.append(create_time)
        t_tuple = tuple(info_values)
        ss = ' = %s , '.join(info_keys)
        id = self.uid_info.get('id')
        if id :
            sql = "update weibo_fensi_info set " + ss + " = %s where id = " + str(id) + " "
            print sql
            print info_values
            ret = self.mysql_con.excute(sql, "one", t_tuple)
            print ret

    def get_uid_info(self):
        self.uid_info = {}
        self.uid_info = self.select_uid_info()
        # self.id_tmp = self.uid_info.get('id')
        # self.uid_info = {'id':318,'uid':5643704257}

    def select_uid_info(self):

        # if not self.id_tmp:
        sql = """
            select id,uid from weibo_fensi_info
                where create_time = 0
                order by id
                limit 1
            """
        # else:
        #     sql = "select id,uid from weibo_fensi_info where create_time = 0 and id > %d order by id limit 1 " % int(
        #         self.id_tmp)
        ret = self.mysql_con.select(sql)
        # print ret
        if ret:
            uid_list_tmp = {}
            for i in ret:
                uid_list_tmp['id'] = i.get("id")
                uid_list_tmp['uid'] = i.get("uid")

            return uid_list_tmp
        else:
            print 'sleep'
            time.sleep(self.spider_sep_per_time)
            return self.select_uid_info()



