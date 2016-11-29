# -*- coding:utf-8 -*-

import webpcone_spider
from rec_driver import *

class PapitubewebpconeSpider(webpcone_spider.WebpconeSpider):
    name = "papitubewebpcone"
    appid = 2806796
    spider_sep_per_time = 300
    # surl = 'http://weibo.com/p/1005055932557435/myfollow?relate=fans#place'
    surl = 'http://weibo.com/p/1005055932557435/follow?relate=fans&page=1#Pl_Official_HisRelation__61'
    # first_url_prefix = 'http://weibo.com/p/1005055932557435/myfollow?cfs=600&relate=fans&t=1&f=1&type=&Pl_Official_RelationFans__91_page='
    # first_url_suffix = '#Pl_Official_RelationFans__91'
    # second_url_prefix = 'http://weibo.com/p/1005055932557435/myfollow?cfs=600&relate=fans&t=1&f=1&type=&Pl_Official_RelationFans__91_page='
    # second_url_suffix = '#Pl_Official_RelationFans__91'
    first_url_prefix = 'http://weibo.com/p/1005055932557435/follow?relate=fans&page='
    first_url_suffix = '#Pl_Official_HisRelation__61'
    second_url_prefix = 'http://weibo.com/p/1005055932557435/follow?relate=fans&page='
    second_url_suffix = '#Pl_Official_HisRelation__61'
    login_uid = 0
    uid_tmp_list = []

    next_page = 0
    largest_page = 5

    mysql_con = ''
    error_file_dir = ""
    error_file = ''
    cookies_user = conf1.MY_COOKIES6

    my_headers = {}
    my_cookies = {}