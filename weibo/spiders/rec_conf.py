#!/usr/bin/env python
# -*- coding: utf-8 -*-

PAPI_COOKIES='YF-V5-G0=4d1671d4e87ac99c27d9ffb0ccd1578f; YF-Ugrow-G0=57484c7c1ded49566c905773d5d00f82; login_sid_t=51268b544bd0b07194a917d9aea293b6; WBStorage=2c466cc84b6dda21|undefined; _s_tentry=-; Apache=3827099389891.8594.1480047211949; SINAGLOBAL=3827099389891.8594.1480047211949; ULV=1480047211970:1:1:1:3827099389891.8594.1480047211949:; SCF=AhbaymuOXxrp802czDmv0TlDfYfOq2CQqM8sprSCHGmnQ2TmOoTtCc2D4YJrWXhWFHc2NSKfnQkKcznPutsRIiI.; SUB=_2A251M8onDeTxGeRJ6lYT-C7OyD-IHXVWSLzvrDV8PUNbmtBeLUf9kW8MLxgqMGcJJaPJdiDZJtNFqIax6A..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFniDsvV_7qRulxkvm70.D25JpX5K2hUgL.FozNeKBE1h5Ee0e2dJLoI7f7qPWDi--4iKnfi-zp; SUHB=0N2ECscvhxRMH-; ALF=1511583223; SSOLoginState=1480047223; un=18600030181; wvr=6; YF-Page-G0=c81c3ead2c8078295a6f198a334a5e82; weiboNotfication=99314793415.02367'
PAPITUBE_COOKIES='YF-Ugrow-G0=56862bac2f6bf97368b95873bc687eef; login_sid_t=0b7d913653935f7fdae186184b37b3a0; YF-V5-G0=cd5d86283b86b0d506628aedd6f8896e; WBStorage=2c466cc84b6dda21|undefined; _s_tentry=-; Apache=2242546933321.319.1479994105131; SINAGLOBAL=2242546933321.319.1479994105131; ULV=1479994105152:1:1:1:2242546933321.319.1479994105131:; SCF=AhbaymuOXxrp802czDmv0TlDfYfOq2CQqM8sprSCHGmnwSTRPFexyl3kL4VQMJKUnyTujWWs_Ru3mCuF8hs-VKs.; SUB=_2A251MptWDeTxGeNH6FAU9SnIyDmIHXVWSYuerDV8PUNbmtBeLXTdkW8IK2PVd9So0s__7svjnyiqHZiGyA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WhlUe_78SzJQPSIJpEya6L.5JpX5K2hUgL.Fo-4e0zfSKMXe0-2dJLoI7y7qPWDUGHb9Btt; SUHB=05iq6mFOA4b7tx; ALF=1511530118; SSOLoginState=1479994119; un=papitube666@163.com; wvr=6; YF-Page-G0=734c07cbfd1a4edf254d8b9173a162eb'

MY_COOKIES1='YF-Ugrow-G0=ad83bc19c1269e709f753b172bddb094; login_sid_t=b18a8b70d9e260e6c9ce9d6e2437c935; YF-V5-G0=8d795ebe002ad1309b7c59a48532ef7d; _s_tentry=-; Apache=6671847013005.414.1480045035741; SINAGLOBAL=6671847013005.414.1480045035741; ULV=1480045035747:1:1:1:6671847013005.414.1480045035741:; SCF=AhbaymuOXxrp802czDmv0TlDfYfOq2CQqM8sprSCHGmn0d3226vFoXIf1WkAY42UHRtMqSyupsK_rZADAEpQmDg.; SUB=_2A251M8YMDeTxGeBO7VUS8CzLzz2IHXVWSLDErDV8PUNbmtBeLUrSkW8u1-s7B3O1DZPLWpCWRsmlrKFDkw..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5qiN1YQRnWrpvsubVp5x6L5JpX5K2hUgL.Foq7SoM0ehzNSh22dJLoIEBLxKnL1hnL1KzLxK-L12zL1KzLxK.L1h5L1-BLxKnL1hnL1Kzt; SUHB=079TxwdeE-6gS5; ALF=1511582172; SSOLoginState=1480046172; un=15527467681; wvr=6; YF-Page-G0=23b9d9eac864b0d725a27007679967df; WBtopGlobal_register_version=5b56985b93d98642'
MY_COOKIES2='YF-Ugrow-G0=ad06784f6deda07eea88e095402e4243; login_sid_t=234b4a2a0691576434697543a0ecb59d; YF-V5-G0=b59b0905807453afddda0b34765f9151; WBStorage=2c466cc84b6dda21|undefined; _s_tentry=-; Apache=321173096643.52997.1480046990331; SINAGLOBAL=321173096643.52997.1480046990331; ULV=1480046990337:1:1:1:321173096643.52997.1480046990331:; SCF=AhbaymuOXxrp802czDmv0TlDfYfOq2CQqM8sprSCHGmn3tyBK8XzZjvXvei9UaLtckmDpP-oB-3xA9IBombfYWk.; SUB=_2A251M8nNDeTxGeBO7VER-C3LzzSIHXVWSLwFrDV8PUNbmtBeLVLAkW9qwF-6aHNyVQJs47PlgM4Xkfju0A..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9Wh7CkG7NCAsZGGAz2xCrDOs5JpX5K2hUgL.Foq7Soe71heNShn2dJLoIEXLxKqL1h.L1hnLxK-LB-BLBK.LxKBLBonLB.BLxKqL1h.L1hnLxKML122LB-et; SUHB=0oUojYFBgehI0y; ALF=1511583005; SSOLoginState=1480047006; un=14784508203; wvr=6; YF-Page-G0=280e58c5ca896750f16dcc47ceb234ed; WBtopGlobal_register_version=5b56985b93d98642'
MY_COOKIES3='YF-V5-G0=4d1671d4e87ac99c27d9ffb0ccd1578f; YF-Ugrow-G0=8751d9166f7676afdce9885c6d31cd61; login_sid_t=c1f23ea338635ec23b9f269576e16de9; WBStorage=2c466cc84b6dda21|undefined; _s_tentry=-; Apache=3431932314468.48.1480047066938; SINAGLOBAL=3431932314468.48.1480047066938; ULV=1480047066944:1:1:1:3431932314468.48.1480047066938:; SCF=AhbaymuOXxrp802czDmv0TlDfYfOq2CQqM8sprSCHGmnUYP0rZtEq154pB4aFyE2reRZXHuOAEogYtRCf0vHTYg.; SUB=_2A251M8mzDeTxGeBO7VER-C3LzT-IHXVWSLx7rDV8PUNbmtBeLXfWkW9ZhPP6UZBVFeTeS8waLOg_IzNtyg..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5KUX07wh.TLZ1WsGnBC4R05JpX5K2hUgL.Foq7Soe71heNSoe2dJLoIEXLxKnL12BL1h5LxKBLBonL1-2LxKML1heL1KnLxKnL12BL1h5LxKBLB.eL1KMt; SUHB=0y0ZSnhko7vdY7; ALF=1511583074; SSOLoginState=1480047075; un=15817013175; wvr=6; YF-Page-G0=00acf392ca0910c1098d285f7eb74a11; WBtopGlobal_register_version=5b56985b93d98642'
MY_COOKIES4='YF-Ugrow-G0=ad06784f6deda07eea88e095402e4243; login_sid_t=c15bdfd2bb2e715500f9bc9ff3f11ba4; YF-V5-G0=c37fc61749949aeb7f71c3016675ad75; WBStorage=2c466cc84b6dda21|undefined; _s_tentry=-; Apache=3016343319206.1694.1480047122018; SINAGLOBAL=3016343319206.1694.1480047122018; ULV=1480047122023:1:1:1:3016343319206.1694.1480047122018:; SCF=AhbaymuOXxrp802czDmv0TlDfYfOq2CQqM8sprSCHGmnOc9vTNtgGxQhqNim-geDEmWmGnKfb4YSuwYQnh2PMRE.; SUB=_2A251M8pODeTxGeBO7VUS8CzIwjyIHXVWSLyGrDV8PUNbmtBeLRnXkW9996OdYa7o1Q6MRnhKr97A8eCfFA..; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9W5yHMZKquRIxjZl2e9DkH7Y5JpX5K2hUgL.Foq7SoM0ehzX1K52dJLoI0qLxK-LB.2L1KeLxK-L1h2LBoMLxKqLB--L12zLxK-LB.2L1KeLxKqLBoeLB-2LxKML1-2L1hqt; SUHB=0auAYt7w4svxh1; ALF=1511583133; SSOLoginState=1480047134; un=14794607619; wvr=6; YF-Page-G0=074bd03ae4e08433ef66c71c2777fd84; WBtopGlobal_register_version=5b56985b93d98642'

error_file_dir = "./error"


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


