#!/usr/bin/env python
# -*- coding: utf-8 -*-

PAPI_COOKIES='SINAGLOBAL=8429665158835.7705.1469175880530; wvr=6; un=18600030181; YF-V5-G0=a5a264208a5b5a42590274f52e6c7304; SCF=Aih4hh1Z4R1PBln4AY5NLT3VNIKRuaSE0wMBHGYKGVYmoNWh5LxhcaHRwqYKCTDZMDDERcRJ9Bu6u6AgwCVDluo.; SUB=_2A2563LrEDeTxGeRJ6lYT-C7OyD-IHXVZq6sMrDV8PUNbmtBeLW_lkW8BH96x2cI_mV8Ry6T4m0dB_8Tm8g..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFniDsvV_7qRulxkvm70.D25JpX5KMhUgL.FozNeKBE1h5Ee0e2dJLoI7f7qPWDi--4iKnfi-zp; SUHB=0S7zdDMxd5WR8n; ALF=1505361427; SSOLoginState=1473825428; YF-Ugrow-G0=ad06784f6deda07eea88e095402e4243; YF-Page-G0=9a31b867b34a0b4839fa27a4ab6ec79f; _s_tentry=-; Apache=8058166487640.87.1473839220694; ULV=1473839220863:25:5:2:8058166487640.87.1473839220694:1473668576929'
MY_COOKIES='SINAGLOBAL=1876600431278.348.1469179441770; wvr=6; SCF=AoJskNKFw1vsIi3GAqp-sgYrab0ZyWBv5BQf9pLddK6sIt3XNPwEuFA_W04T0oDAQcQ8u-Whmq1P4B1Z7bRbRik.; SUB=_2A2563M6sDeTxGeRO7lsY8S7OzzuIHXVZq6dkrDV8PUNbmtBeLVfYkW9h1VXI_swirZNr8SAkJPL26PnYUw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5bBR5Dhx5.cFfenb69ck4I5JpX5KMhUgL.Foz7SK.4eK5EShM2dJLoIEp_qPiu9NHDTCH81FHFxCHFxCH81FHWSE-RebH8Sb-4SCHFeFH8Sb-RxFHWxBtt; SUHB=05iLQFjWw3jk56; ALF=1505358458; SSOLoginState=1473822460; YF-V5-G0=fec5de0eebb24ef556f426c61e53833b; YF-Page-G0=340a8661f2b409bf3ea4c8981c138854; _s_tentry=login.sina.com.cn; Apache=4597931012976.915.1473822471880; UOR=,,login.sina.com.cn; ULV=1473822471956:29:7:2:4597931012976.915.1473822471880:1473749382681; YF-Ugrow-G0=3a02f95fa8b3c9dc73c74bc9f2ca4fc6'



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


