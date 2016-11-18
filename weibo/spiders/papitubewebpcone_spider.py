# -*- coding:utf-8 -*-

import webpcone_spider
from rec_driver import *

class PapitubewebpconeSpider(webpcone_spider.WebpconeSpider):
    name = "papitubewebpcone"
    appid = 2806796
    spider_sep_per_time = 3600
    surl = 'http://weibo.com/p/1005055932557435/myfollow?relate=fans#place'
    first_url_prefix = 'http://weibo.com/p/1005055932557435/myfollow?cfs=600&relate=fans&t=1&f=1&type=&Pl_Official_RelationFans__91_page='
    first_url_suffix = '#Pl_Official_RelationFans__91'
    second_url_prefix = 'http://weibo.com/p/1005055932557435/myfollow?cfs=600&relate=fans&t=1&f=1&type=&Pl_Official_RelationFans__91_page='
    second_url_suffix = '#Pl_Official_RelationFans__91'
    login_uid = 0
    uid_tmp_list = []

    next_page = 0
    largest_page = 250

    mysql_con = ''
    error_file_dir = ""
    error_file = ''
    cookies_user = conf1.PAPITUBE_COOKIES

    my_headers = {}
    my_cookies = {}