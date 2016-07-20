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


#surl
#start_search_page,end_search_page
#url_fans
#my_cookies

class WebpcSpider(scrapy.spiders.Spider):
    name = "webpc"
    allowed_domains = ['weibo.com','weibo.cn','sina.com.cn']
    # start_urls=['http://m.weibo.cn']
    surl = 'http://weibo.com/2714280233/follow?from=page_100505&wvr=6&mod=headfollow#place'
    page_search_url=''
    start_page=1
    run_page=0
    start_search_page=0
    end_search_page=250
    login_uid=0
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

    my_headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding':'gzip,deflate,sdch',
        'Accept-Language':'zh-CN,zh;q=0.8',
        # 'Cache-Control':'no-cache',
        'Connection':'keep-alive',
        'Host':'weibo.com',
        # 'Pragma':'no-cache',
        'Referer':'http://weibo.com/p/1005055946421838/home?from=page_100505&mod=TAB&is_all=1',
        'Upgrade-Insecure-Requests':'1',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36',
    }


# 'YF-Ugrow-G0=57484c7c1ded49566c905773d5d00f82; ' \
# 'YF-V5-G0=bb389e7e25cccb1fadd4b1334ab013c1; ' \
# 'WBStore=8ca40a3ef06ad7b2|undefined; ' \
# '_s_tentry=-; ' \
# 'Apache=3013729271600.356.1468984228116; ' \
# 'SINAGLOBAL=3013729271600.356.1468984228116; ' \
# 'ULV=1468984228129:1:1:1:3013729271600.356.1468984228116:; ' \
# 'SCF=Aih4hh1Z4R1PBln4AY5NLT3VNIKRuaSE0wMBHGYKGVYmHRMNMJVVdZ9Y4iYWKWDYus8A3p3aPPkZ6zlwQDadGUs.; ' \
# 'SUB=_2A256ipvmDeTxGeRJ6lYT-C7OyD-IHXVZ4YourDV8PUNbmtBeLU_VkW8yAbQRExZ4YCZW-8iVhIE8aNwIiQ..; ' \
# 'SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFniDsvV_7qRulxkvm70.D25JpX5K2hUgL.FozNeKBE1h5Ee0e2dJLoI7f7qPWDi--4iKnfi-zp; ' \
# 'SUHB=0V5UloHPDCAdL9; ' \
# 'ALF=1500520246; ' \
# 'SSOLoginState=1468984246; ' \
# 'un=18600030181; ' \
# 'wvr=6; ' \
# 'wb_bub_hot_2714280233=1; ' \
# 'YF-Page-G0=1ac418838b431e81ff2d99457147068c'

    my_cookies = {
        'YF-Page-G0':'1ac418838b431e81ff2d99457147068c',
        'YF-Ugrow-G0':'57484c7c1ded49566c905773d5d00f82',
        'YF-V5-G0':'bb389e7e25cccb1fadd4b1334ab013c1',
        'SINAGLOBAL': '3013729271600.356.1468984228116',
        '_s_tentry': '-',
        'Apache': '3013729271600.356.1468984228116',
        'ULV': '1468984228129:1:1:1:3013729271600.356.1468984228116:',
        'SUHB': '0V5UloHPDCAdL9',
        'SSOLoginState': '1468984246',
        'un': '18600030181',
        'wvr': '6',
        'ALF': '1500520246',
        'SUBP': '0033WrSXqPxfM725Ws9jqgMF55529P9D9WFniDsvV_7qRulxkvm70.D25JpX5K2hUgL.FozNeKBE1h5Ee0e2dJLoI7f7qPWDi--4iKnfi-zp',
        'SCF':'Aih4hh1Z4R1PBln4AY5NLT3VNIKRuaSE0wMBHGYKGVYmHRMNMJVVdZ9Y4iYWKWDYus8A3p3aPPkZ6zlwQDadGUs.',
        'SUB':'_2A256ipvmDeTxGeRJ6lYT-C7OyD-IHXVZ4YourDV8PUNbmtBeLU_VkW8yAbQRExZ4YCZW-8iVhIE8aNwIiQ..',
        'wb_bub_hot_2714280233':'1',
        'WBStore':'8ca40a3ef06ad7b2|undefined',
        # 'UOR':'datagrand.com,widget.weibo.com,datagrand.com',
    }

    def start_requests(self):

        self.mysql_con = PyMysql(conf1.MYSQL_URL, conf1.MYSQL_PORT, conf1.MYSQL_USER, conf1.MYSQL_PASSWD, conf1.MYSQL_DG_DB)

        return [scrapy.Request(url=self.surl , meta={'cookiejar':0} , cookies=self.my_cookies , callback=self.see_home
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
        #
        # with open('webpage', 'ab') as f:
        #     f.write(response.body)

        # response.xpath('')
        url_tmp = response.url
        url_tmp = str(url_tmp)
        m1 = re.match(r'.*\/(\d+)\/.*', url_tmp)
        if m1:
            self.login_uid = m1.groups()[0]

            # url_fans='http://weibo.com/' + str(self.login_uid) + '/fans?rightmod=1&wvr=6'
            url_fans='http://weibo.com/2714280233/fans?cfs=600&relate=fans&t=1&f=1&type=&Pl_Official_RelationFans__103_page=120#Pl_Official_RelationFans__103'
            print "next_url"
            print url_fans

            return [scrapy.Request(url=url_fans, meta={'cookiejar': 0}, dont_filter=True, callback=self.see_list
                                   )]


    def see_list(self,response):

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

        str1=response.body
        if not self.start_search_page:
            m_start = re.match(r'.*page=([\d]+).*', response.url)
            if m_start:
                current_page_tmp = m_start.groups()[0]
                self.start_search_page = int(current_page_tmp)

        # ul = response.xpath('//ul[contains(@class, "follow_list")]').extract()
        # print "ul"
        # print ul
        str1=str(str1)
        str2 = str1.replace("\n", "")
        str2 = str2.replace("\\n", "")
        m1 = re.match(r'.*\<!--粉丝列表--\>(.*)', str2)
        if m1:
            str2 = m1.groups()[0]
            # with open('ul', 'wb') as f:
            #     f.write(str2)
            # ul = Selector(text=str2).xpath('//ul[contains(@class, "follow_list")]').extract()
            uid_dict_tmp={}
            m1 = re.findall(r'\/u\\/([\d]+)\?', str2)
            if m1:
                for i in m1:

                    uid_dict_tmp[i]=1


            self.uid_tmp_list = uid_dict_tmp.keys()
            self.insert_uid()
            self.uid_tmp_list=[]

            time_now = time.strftime('%Y-%m-%d %X', time.gmtime(time.time()))
            run_page_str = time_now + '---' + response.url + "\r\n"
            with open('run_page', 'ab') as f:
                f.write(run_page_str)

            m2 = re.match(r'.*page next S_txt1 S_line1\\\" href=\\\"([^\"]*)\".*', str2)
            if m2:
                str3=m2.groups()[0]
                str3=str3.replace("\\","")

                next_url='http://weibo.com'+str3

                print "next_url"
                print next_url

                m_end = re.match(r'.*page=([\d]+).*', next_url)
                if m_end:
                    next_page_tmp = m_end.groups()[0]

                    next_page_tmp=int(next_page_tmp)

                    if next_page_tmp>self.end_search_page:
                        
                        return
                    if next_page_tmp<self.start_search_page:
                        replace_rule = re.compile("page=[\d]+")
                        next_url = re.sub(replace_rule, 'page='+ str(self.start_search_page) , next_url)
                        pass
                else:
                    # return
                    pass



                time.sleep(1)
                return [scrapy.Request(url=next_url, meta={'cookiejar': 0}, dont_filter=True,callback=self.see_list
                                       )]
            else:
                time_now = time.strftime('%Y-%m-%d %X', time.gmtime(time.time()))
                run_error_str = time_now + '---' + response.url + "---" + "out 1" + "\r\n"
                with open('run_page_error', 'ab') as f:
                    f.write(run_error_str)
                return [scrapy.Request(url=response.url, meta={'cookiejar': 0},dont_filter=True, callback=self.see_list
                                       )]

        else:
            time_now = time.strftime('%Y-%m-%d %X', time.gmtime(time.time()))
            run_error_str = time_now + '---' + response.url + "---" + "out 2" + "\r\n"
            with open('run_page_error', 'ab') as f:
                f.write(run_error_str)
            time.sleep(1)
            return [scrapy.Request(url=response.url, meta={'cookiejar': 0},dont_filter=True, callback=self.see_list
                                   )]



    def see_other_list(self,response):

        pass


    def insert_uid(self):
        if not self.uid_tmp_list:
            return
        t_tuple = []
        for i in self.uid_tmp_list:
            i=int(i)
            t_tuple_tmp = tuple([i])
            t_tuple.append(t_tuple_tmp)

        sql = """
            insert into weibo_fensi_info (
                `uid`
            ) values (%s)

        """
        ret = self.mysql_con.excute(sql, "many", t_tuple)

        print ret

