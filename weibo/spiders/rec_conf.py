#!/usr/bin/env python
# -*- coding: utf-8 -*-

PAPI_COOKIES='SINAGLOBAL=8429665158835.7705.1469175880530; wvr=6; YF-Ugrow-G0=1eba44dbebf62c27ae66e16d40e02964; SCF=Aih4hh1Z4R1PBln4AY5NLT3VNIKRuaSE0wMBHGYKGVYmFTvCjKQLUQPwRP-BgGr6Fsg1qhlgnBkBvHsQbQVCvJc.; SUB=_2A256prt8DeTxGeRJ6lYT-C7OyD-IHXVZ1au0rDV8PUNbmtBeLUzjkW8CWxO_gsPQZ3b71xsDpNUqVVcAag..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFniDsvV_7qRulxkvm70.D25JpX5KMhUgL.FozNeKBE1h5Ee0e2dJLoI7f7qPWDi--4iKnfi-zp; SUHB=0la0PZJZMMMF4X; ALF=1501822636; SSOLoginState=1470286636; YF-V5-G0=73b58b9e32dedf309da5103c77c3af4f; _s_tentry=login.sina.com.cn; Apache=9796859648416.23.1470286632062; ULV=1470286632285:13:5:5:9796859648416.23.1470286632062:1470276371047; YF-Page-G0=734c07cbfd1a4edf254d8b9173a162eb; UOR=,,login.sina.com.cn'
MY_COOKIES='wb_bub_hot_5946421838=1; wb_bub_hot_2059910247=1; SINAGLOBAL=1876600431278.348.1469179441770; wvr=6; SCF=AoJskNKFw1vsIi3GAqp-sgYrab0ZyWBv5BQf9pLddK6s7k86uIxk4Eb5n2UiHtS9svmjeuvYv_2cMarig0944ZU.; SUB=_2A256ptPVDeTxGeRO7lsY8S7OzzuIHXVZ0kIdrDV8PUNbmtBeLUXSkW-YNzMILYY18JzU_caCL5gLfsFKqg..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5bBR5Dhx5.cFfenb69ck4I5JpX5KMhUgL.Foz7SK.4eK5EShM2dJLoIEp_qPiu9NHDTCH81FHFxCHFxCH81FHWSE-RebH8Sb-4SCHFeFH8Sb-RxFHWxBtt; SUHB=0sqw9UGnmAtRvy; ALF=1501812484; SSOLoginState=1470276485; YF-V5-G0=55f24dd64fe9a2e1eff80675fb41718d; _s_tentry=login.sina.com.cn; Apache=8565865349955.856.1470276489149; ULV=1470276489195:13:5:5:8565865349955.856.1470276489149:1470191920666; UOR=,,login.sina.com.cn; YF-Page-G0=f994131fbcce91e683b080a4ad83c421'



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


