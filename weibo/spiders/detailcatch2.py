# -*- coding:utf-8 -*-

import detailcatch
from rec_driver import *


class Detailcatch2Spider(detailcatch.DetailcatchSpider):
    name = "detailcatch2"

    cookies_user = conf1.MY_COOKIES4



    def select_uid_info(self):

        # if not self.id_tmp:
        sql = """
            select id,uid from weibo_fensi_info
                where create_time = 0
                order by id
                limit 2000,1
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



