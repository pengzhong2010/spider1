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


    mysql_con = ''

    my_cookies = {}

    def start_requests(self):
        cookies_list = conf1.MY_COOKIES.split('; ')

        for i in cookies_list:
            tmp = i.split('=')

            k = tmp[0]

            v = tmp[1]

            self.my_cookies.setdefault(k, v)

        self.mysql_con = PyMysql(conf1.MYSQL_URL, conf1.MYSQL_PORT, conf1.MYSQL_USER, conf1.MYSQL_PASSWD,
                                 conf1.MYSQL_DG_DB)

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



        # with open('commentlist', 'wb') as f:
        #     f.write(response.body)
        str1 = response.body
        str1 = str1.replace('\r\n', '')
        str1 = str1.replace('\t', '')
        str1 = str1.replace('\\r\\n', '')
        str1 = str1.replace('\\n', '')
        str1 = str1.replace('\\t', '')
        list1 = Selector(text=str1).xpath('//script/text()').extract()
        for str_html in list1:
            tag = 'FM.view({"ns":"pl.content.homeFeed.index","domid":"Pl_Official_MyProfileFeed__24"'
            m4 = re.match(
                r'.*FM.view\(\{\"ns\":\"pl\.content\.homeFeed\.index\",\"domid\":\"Pl_Official_MyProfileFeed__24\"(.*)',
                str_html)
            if m4:
                m2 = re.match(r'.*\"html\":\"(.*)', str_html)
                if m2:
                    str2 = m2.groups()[0]
                    str2 = str2.replace('\\', '')
                    list3 = Selector(text=str2).xpath('//div[contains(@class, "WB_detail")]')
                    blog_list=[]
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
                    # print blog_list
                    self.check_blog(blog_list)
                return


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

                    t_tuple = tuple([blog_id, blog_url, blog_create_time, blog_title])

                    sql = """
                                    insert into weibo_blog (
                                        blog_id,
                                        url,
                                        create_time,
                                        title
                                    ) values (%s,%s,%s,%s)

                                """
                    ret = self.mysql_con.excute(sql, "one", t_tuple)
                    # print ret