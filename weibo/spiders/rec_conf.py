#!/usr/bin/env python
# -*- coding: utf-8 -*-

PAPI_COOKIES='SINAGLOBAL=8429665158835.7705.1469175880530; un=18600030181; YF-Ugrow-G0=1eba44dbebf62c27ae66e16d40e02964; SCF=Aih4hh1Z4R1PBln4AY5NLT3VNIKRuaSE0wMBHGYKGVYmC3y-JTuAIV8seco_5bffux15ItGGjPqU7QaE2Ol5LyA.; SUB=_2A251Hf70DeTxGeRJ6lYT-C7OyD-IHXVWa1c8rDV8PUNbmtBeLRj5kW9He3BbmqHnMyD-h-0eBpo7SobySw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFniDsvV_7qRulxkvm70.D25JpX5KMhUgL.FozNeKBE1h5Ee0e2dJLoI7f7qPWDi--4iKnfi-zp; SUHB=0mxlnH-eiYtkTJ; ALF=1509605924; SSOLoginState=1478069924; wvr=6; YF-V5-G0=3737d4e74bd7e1b846a326489cdaf5ab; _s_tentry=login.sina.com.cn; Apache=1703984625829.158.1478069929153; ULV=1478069929236:39:2:2:1703984625829.158.1478069929153:1477994791565; YF-Page-G0=074bd03ae4e08433ef66c71c2777fd84; UOR=,,login.sina.com.cn; weiboNotfication=978918311785.189'
MY_COOKIES='SINAGLOBAL=1876600431278.348.1469179441770; UOR=,,www.psjia.com; login_sid_t=41bde58bed84df525da328db3ab76673; YF-V5-G0=a2489c19ecf98bbe86a7bf6f0edcb071; _s_tentry=-; Apache=7628121213056.147.1478070556743; ULV=1478070557446:47:1:1:7628121213056.147.1478070556743:1477534868534; SCF=AoJskNKFw1vsIi3GAqp-sgYrab0ZyWBv5BQf9pLddK6s5fwNh6GT71coUKIVqkKmL-BVa9IB91HIbeBBE5Rv7vE.; SUB=_2A251HeFzDeTxGeNJ71UU9CjNzzWIHXVWa1W7rDV8PUNbmtBeLVLnkW9uNlJBmA8UBBKkYUOBa5YSF45zzQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW_ETNhr.83BNpbYTwmiWRr5JpX5K2hUgL.Fo-NShMfShqpSh.2dJLoIEBLxKnLB.-LB.-LxKnLBKML1hzLxKqL1K-LBo5LxKqL12BLB--t; SUHB=0N2lkNcyxxa2qv; ALF=1509606562; SSOLoginState=1478070563; YF-Page-G0=3d55e26bde550ac7b0d32a2ad7d6fa53'



IS_TABLE_ONLINE = False
IS_REDIS_ONLINE = False

MYSQL_URL = "rdsq3zsso4e737w4gwjq.mysql.rds.aliyuncs.com"
MYSQL_USER = "thirdparty"
MYSQL_PASSWD = "Thirdparty123"
MYSQL_PORT = 3306
# MYSQL_PROMOTE_DB = "promote"
MYSQL_DG_DB = "thirdparty"
#
# if IS_TABLE_ONLINE:  #online
#     MYSQL_URL = "rdsq3zsso4e737w4gwjq.mysql.rds.aliyuncs.com"
#     MYSQL_USER = "thirdparty"
#     MYSQL_PASSWD = "Thirdparty123"
#     MYSQL_PORT = 3306
#     MYSQL_THIRDPARTY_DB = "thirdparty"
# else:               #test
#     MYSQL_URL = "rdsq3zsso4e737w4gwjq.mysql.rds.aliyuncs.com"
#     MYSQL_USER = "thirdparty"
#     MYSQL_PASSWD = "Thirdparty123"
#     MYSQL_PORT = 3306
#     MYSQL_THIRDPARTY_DB = "thirdparty"


if IS_REDIS_ONLINE:  #online
    SITE_REC_HOST = "10.172.91.36"
else:               #test
    SITE_REC_HOST = "10.170.173.139"


SITE_REC_PORT = 6388
SITE_REC_PAPI_WEIBO_SPIDER_DB = 14

SITE_REC_PASSWD = "Abe#11Ba!bcEfhDgvPaMr"
SITE_REC_CACHE_TIME = 0
SITE_REC_EXPIRE_SECONDS = 15 * 24 * 3600


