#!/usr/bin/env python
# -*- coding: utf-8 -*-

PAPI_COOKIES='SINAGLOBAL=8429665158835.7705.1469175880530; un=18600030181; wvr=6; YF-Ugrow-G0=1eba44dbebf62c27ae66e16d40e02964; SCF=Aih4hh1Z4R1PBln4AY5NLT3VNIKRuaSE0wMBHGYKGVYm2w9g8l8VcEv-PhAhVZ9BL1OFGk7VsMkoWysiAXi-EkE.; SUB=_2A256nGi0DeTxGeRJ6lYT-C7OyD-IHXVZ6N18rDV8PUNbmtBeLWbFkW9_Ip7ZxmOxrmA0XnBa7ezFmqwm6A..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFniDsvV_7qRulxkvm70.D25JpX5KMhUgL.FozNeKBE1h5Ee0e2dJLoI7f7qPWDi--4iKnfi-zp; SUHB=0btN856vSLdOXJ; ALF=1501121635; SSOLoginState=1469585636; YF-V5-G0=bcfc495b47c1efc5be5998b37da5d0e4; _s_tentry=login.sina.com.cn; Apache=4899092567240.762.1469585643230; ULV=1469585643302:7:7:4:4899092567240.762.1469585643230:1469532261026; UOR=,,login.sina.com.cn; YF-Page-G0=27b9c6f0942dad1bd65a7d61efdfa013'
MY_COOKIES='wb_bub_hot_5946421838=1; wb_bub_hot_2059910247=1; wvr=6; SINAGLOBAL=1876600431278.348.1469179441770; SCF=AoJskNKFw1vsIi3GAqp-sgYrab0ZyWBv5BQf9pLddK6sJBP75Z_wOLltRDGUYUiZbQHqSpSfUwDarBl2W0nvvrU.; SUB=_2A256nGn0DeTxGeRO7lsY8S7OzzuIHXVZ6Nw8rDV8PUNbmtBeLUankW-AOpEJsP5r89ZXPT9Eymw-ui1p5w..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5bBR5Dhx5.cFfenb69ck4I5JpX5KMhUgL.Foz7SK.4eK5EShM2dJLoIEp_qPiu9NHDTCH81FHFxCHFxCH81FHWSE-RebH8Sb-4SCHFeFH8Sb-RxFHWxBtt; SUHB=08JKu_YJw-H-fN; ALF=1501121827; SSOLoginState=1469585829; YF-V5-G0=c998e7c570da2f8537944063e27af755; _s_tentry=login.sina.com.cn; Apache=2560614859685.302.1469585839200; ULV=1469585839967:5:5:3:2560614859685.302.1469585839200:1469502914076; UOR=,,login.sina.com.cn; YF-Page-G0=ab26db581320127b3a3450a0429cde69'



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


