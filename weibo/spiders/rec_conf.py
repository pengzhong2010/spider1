#!/usr/bin/env python
# -*- coding: utf-8 -*-

PAPI_COOKIES='SINAGLOBAL=8429665158835.7705.1469175880530; un=18600030181; wvr=6; TC-Ugrow-G0=0149286e34b004ccf8a0b99657f15013; SCF=Aih4hh1Z4R1PBln4AY5NLT3VNIKRuaSE0wMBHGYKGVYmcjF8WyHchb2hL7l85-DFhRbKrs3TjupKTU2Jyk9BoqE.; SUB=_2A256kLedDeTxGeRJ6lYT-C7OyD-IHXVZ565VrDV8PUNbmtAKLRTikW9NgP4MXAwnUqijvAU8q4MN-nYEzA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFniDsvV_7qRulxkvm70.D25JpX5KMhUgL.FozNeKBE1h5Ee0e2dJLoI7f7qPWDi--4iKnfi-zp; SUHB=0k1z_e6lZVdFVn; ALF=1500904266; SSOLoginState=1469368269; TC-V5-G0=05e7a45f4d2b9f5b065c2bea790496e2; TC-Page-G0=cdcf495cbaea129529aa606e7629fea7; _s_tentry=login.sina.com.cn; Apache=8812233658740.01.1469368271944; ULV=1469368271993:4:4:1:8812233658740.01.1469368271944:1469288289871; UOR=,,login.sina.com.cn'
MY_COOKIES='wb_bub_hot_5946421838=1; wb_bub_hot_2059910247=1; wvr=6; SINAGLOBAL=1876600431278.348.1469179441770; SCF=AoJskNKFw1vsIi3GAqp-sgYrab0ZyWBv5BQf9pLddK6sk9LoSFSn32H4njdn8mJDcAk9oZxv-fr_FeO2J-XgvVE.; SUB=_2A256kQ6CDeTxGeRO7lsY8S7OzzuIHXVZ52dKrDV8PUNbmtBeLROgkW-IYXYMSSEz6MwXloSVl_PyWyJdFQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5bBR5Dhx5.cFfenb69ck4I5JpX5KMhUgL.Foz7SK.4eK5EShM2dJLoIEp_qPiu9NHDTCH81FHFxCHFxCH81FHWSE-RebH8Sb-4SCHFeFH8Sb-RxFHWxBtt; SUHB=0pHAjxqEoWzqSB; ALF=1500951121; SSOLoginState=1469415122; YF-V5-G0=1e772c9803ad8482528fd25e77086251; _s_tentry=login.sina.com.cn; Apache=2172332953196.019.1469415132439; ULV=1469415132894:3:3:1:2172332953196.019.1469415132439:1469203647840; YF-Page-G0=f0e89c46e7ea678e9f91d029ec552e92; UOR=,,login.sina.com.cn'



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


