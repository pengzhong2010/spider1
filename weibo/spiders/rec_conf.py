#!/usr/bin/env python
# -*- coding: utf-8 -*-

PAPI_COOKIES='SINAGLOBAL=8429665158835.7705.1469175880530; un=18600030181; wvr=6; YF-Ugrow-G0=1eba44dbebf62c27ae66e16d40e02964; SCF=Aih4hh1Z4R1PBln4AY5NLT3VNIKRuaSE0wMBHGYKGVYmho4iZghFJACkTsV9RG-a1SXN-MlAMl4pT_u7ti_Wbuw.; SUB=_2A256nRwhDeTxGeRJ6lYT-C7OyD-IHXVZ6wrprDV8PUNbmtBeLRmlkW84GOFK4gK33mMZvfFNeU1BIARQLg..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFniDsvV_7qRulxkvm70.D25JpX5KMhUgL.FozNeKBE1h5Ee0e2dJLoI7f7qPWDi--4iKnfi-zp; SUHB=0y0oMT80djmVgy; ALF=1501208559; SSOLoginState=1469672563; YF-V5-G0=c99031715427fe982b79bf287ae448f6; _s_tentry=login.sina.com.cn; Apache=90757279970.8789.1469672573324; ULV=1469672574001:8:8:5:90757279970.8789.1469672573324:1469585643302; UOR=,,login.sina.com.cn; YF-Page-G0=206250b160696bcef4885d60544c84d5'
MY_COOKIES='wb_bub_hot_5946421838=1; wb_bub_hot_2059910247=1; wvr=6; SINAGLOBAL=1876600431278.348.1469179441770; SCF=AoJskNKFw1vsIi3GAqp-sgYrab0ZyWBv5BQf9pLddK6sFPj5EFtgwN-7ef7R7KmUZFHn4cvA3I2tGkIb0pJlsQY.; SUB=_2A256nRzlDeTxGeRO7lsY8S7OzzuIHXVZ6wktrDV8PUNbmtBeLVjbkW9BU3twcq8mZFqKCFjigtKLSzp9UQ..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5bBR5Dhx5.cFfenb69ck4I5JpX5KMhUgL.Foz7SK.4eK5EShM2dJLoIEp_qPiu9NHDTCH81FHFxCHFxCH81FHWSE-RebH8Sb-4SCHFeFH8Sb-RxFHWxBtt; SUHB=0k1z3bRF5Vf-aZ; ALF=1501208628; SSOLoginState=1469672629; YF-V5-G0=1312426fba7c62175794755e73312c7d; _s_tentry=login.sina.com.cn; Apache=4997994552832.097.1469672643219; ULV=1469672643623:7:7:5:4997994552832.097.1469672643219:1469589333572; YF-Page-G0=f994131fbcce91e683b080a4ad83c421; UOR=,,login.sina.com.cn'



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


