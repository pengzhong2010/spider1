# -*- coding:utf-8 -*-

import comment_spider

class PapitubecommentSpider(comment_spider.CommentSpider):
    name = "papitubecomment"
    spider_sep_per_time = 3600
    #surl = 'http://weibo.com/xiaopapi/profile?rightmod=1&wvr=6&mod=personnumber&is_all=1'
    surl = 'http://www.weibo.com/5932557435/profile?rightmod=1&wvr=6&mod=personnumber&is_all=1'
    first_url_prefix = 'http://weibo.com/aj/v6/comment/big?ajwvr=6&id='
    first_url_suffix = '&page='
    blog_list = ''
    blog_list_len = 0
    blog_list_key = 0
    comment_page = 1
    url_page_demo = ''
    blog_id = ''

    mysql_con = ''
    my_cookies = {}
    error_file_dir = ""
    error_file = ''
    appid = 2806796