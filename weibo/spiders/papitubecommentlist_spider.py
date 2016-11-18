# -*- coding:utf-8 -*-

import commentlist_spider

class PapitubecommentlistSpider(commentlist_spider.CommentlistSpider):
    name = "papitubecommentlist"
    #surl = 'http://weibo.com/xiaopapi/profile?rightmod=1&wvr=6&mod=personnumber&is_all=1'
    surl = 'http://www.weibo.com/5932557435/profile?rightmod=1&wvr=6&mod=personnumber&is_all=1'

    spider_sep_per_time = 86400

    mysql_con = ''

    my_cookies = {}
    error_file_dir = ""
    error_file = ''
    appid = 2806796