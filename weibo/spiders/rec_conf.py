#!/usr/bin/env python
# -*- coding: utf-8 -*-

PAPI_COOKIES='SINAGLOBAL=8429665158835.7705.1469175880530; wvr=6; YF-Ugrow-G0=b02489d329584fca03ad6347fc915997; login_sid_t=69b2499e80f6ec7ff3fbb1c658b7258e; YF-V5-G0=f59276155f879836eb028d7dcd01d03c; WBStorage=86fb700cbf513258|undefined; _s_tentry=login.sina.com.cn; UOR=,,login.sina.com.cn; Apache=2035924917376.2773.1474450135331; ULV=1474450135341:27:7:3:2035924917376.2773.1474450135331:1474252034783; SCF=Aih4hh1Z4R1PBln4AY5NLT3VNIKRuaSE0wMBHGYKGVYmh9N6femDJCUADunEAeKAa8A4Axol050smH4Xd5AseLs.; SUB=_2A2565iKODeTxGeRJ6lYT-C7OyD-IHXVZkhNGrDV8PUNbmtBeLVDekW9io-8XjbIg1kaZFZbX0Ooy-UPDLw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFniDsvV_7qRulxkvm70.D25JpX5K2hUgL.FozNeKBE1h5Ee0e2dJLoI7f7qPWDi--4iKnfi-zp; SUHB=0tKbIVSMZk9WoG; ALF=1505986141; SSOLoginState=1474450142; un=18600030181; YF-Page-G0=b5853766541bcc934acef7f6116c26d1'
MY_COOKIES='SINAGLOBAL=1876600431278.348.1469179441770; UOR=,,login.sina.com.cn; un=contact@datagrand.com; YF-Ugrow-G0=ad06784f6deda07eea88e095402e4243; login_sid_t=6e331892af16b7eefd9088281c653327; YF-V5-G0=2a21d421b35f7075ad5265885eabb1e4; _s_tentry=-; Apache=7779725992586.464.1474449705332; ULV=1474449705337:35:13:5:7779725992586.464.1474449705332:1474358007717; SCF=AoJskNKFw1vsIi3GAqp-sgYrab0ZyWBv5BQf9pLddK6sJzJcUFlQnPVhcd36SG-2F8OzwhXnwbAga_qCgkEEVfk.; SUB=_2A2565iG7DeTxGeNJ71UU9CjNzzWIHXVZkhRzrDV8PUNbmtBeLWz2kW9fq9nLGliez_H1QzBIlIUGzOfzRg..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW_ETNhr.83BNpbYTwmiWRr5JpX5K2hUgL.Fo-NShMfShqpSh.2dJLoIEBLxKnLB.-LB.-LxKnLBKML1hzLxKqL1K-LBo5LxKqL12BLB--t; SUHB=0G0-x1h-z4sQ6q; ALF=1505985899; SSOLoginState=1474449899; YF-Page-G0=59104684d5296c124160a1b451efa4ac'



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


