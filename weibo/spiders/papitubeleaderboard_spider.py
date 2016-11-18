# -*- coding:utf-8 -*-

import leaderboard_spider
from rec_driver import *

class PapitubeleaderboardSpider(leaderboard_spider.LeaderboardSpider):
    name = "papitubeleaderboard"
    #surl = 'http://weibo.com/xiaopapi/profile?rightmod=1&wvr=6&mod=personnumber&is_all=1'
    surl = 'http://www.weibo.com/5932557435/profile?rightmod=1&wvr=6&mod=personnumber&is_all=1'
    spider_sep_per_time = 86400
    blog_list = ''
    blog_list_key = 0
    blog_list_len = 0
    blog_id = 0

    mysql_con = ''
    my_cookies = {}
    error_file_dir = ""
    error_file = ''
    cookies_user = conf1.MY_COOKIES2
    appid = 2806796