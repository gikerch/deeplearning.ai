# coding: utf-8

import requests
import json
import pandas as pd
from pandas import DataFrame
import time
s = time.clock()
# # 验证码地址
# valicode_url = 'http://202.120.82.182:9090/captcha.jpg'
# login_url = "http://202.120.82.182:9090/sys/login"

# # 保存验证码到本地
# picture = requests.get(valicode_url)
# local = open('vali_pic.jpg','wb')
# local.write(picture.content)
# local.close()

# # 手动输入验证码
# valicode = raw_input(u'输入验证码：'.encode('gbk'))
# print requests.utils.dict_from_cookiejar(picture.cookies)

# # # 管理cookies对象
# # # >>> jar = requests.cookies.RequestsCookieJar()
# # # >>> jar.set('tasty_cookie', 'yum', domain='httpbin.org', path='/cookies')
# # # >>> jar.set('gross_cookie', 'blech', domain='httpbin.org', path='/elsewhere')
# # # >>> url = 'http://httpbin.org/cookies'
# # # >>> r = requests.get(url, cookies=jar)
# # # >>> r.text

# # form-data
# payload = "username=nic&password=nic3081&captcha=%s" %valicode

# # headers
# headers = {
#     # 'cookie': "JSESSIONID=4b7033ae-bcda-43fb-8cec-3414d4dd9726",
#     'host': "202.120.82.182:9090",

#     'text/html':"application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
#     'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
#     'x-requested-with': "XMLHttpRequest",
#     'content-type': "application/x-www-form-urlencoded; charset=UTF-8",
#     'cache-control': "no-cache",
#     'Accept-Encoding':'gzip, eflate, sdch'
#     }

# response1 = requests.request("POST", login_url, allow_redirects=False, cookies=requests.utils.dict_from_cookiejar(picture.cookies), data=payload, headers=headers)
# print response1.text
# print requests.utils.dict_from_cookiejar(response1.cookies)
# # headers = {
# #     # 'cookie': "JSESSIONID=4b7033ae-bcda-43fb-8cec-3414d4dd9726",
# #     'host': "202.120.82.182:9090",
# #     'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
# #     'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
# #     'cache-control': "no-cache",
# #     'Accept-Encoding':'gzip, deflate, sdch',
# #     'Upgrade-Insecure-Requests':'1'
# #     }
 
# # print requests.utils.dict_from_cookiejar(picture.cookies)
# data_url = 'http://202.120.82.182:9090/currentURL/rtlList?limit=100&page=2&stime=2017-10-26&etime=2017-10-26&sip=&dip=&platformId=&websiteId=&username=&domain=&url=&action=&platform=&browser=&line=&dir=&initParam='
# # r2 = requests.get(data_url,cookies=requests.utils.dict_from_cookiejar(picture.cookies),headers=headers)
# # r2.encoding = 'utf-8'
# # print requests.utils.dict_from_cookiejar(r2.cookies)
# # print r2.text


# cookies = requests.utils.dict_from_cookiejar(picture.cookies)
# cookie = ''
# for k,v in cookies.iteritems():
#     cookie+=k+'='+v+';rmbUser=true'
# print cookie



url = "http://202.120.82.182:9090/currentURL/rtlList"

querystring = {"limit":"100","page":"2","stime":"2017-10-21","etime":"2017-10-21","sip":"","dip":"","platformId":"","websiteId":"","username":"","domain":"","url":"","action":"","platform":"","browser":"","line":"","dir":"","initParam":""}
headers = {
    'Cookie':'JSESSIONID=811db904-f275-40f6-877f-c6d22c520a14; rmbUser=true; username=nic; password=nic3081',
    'host': "202.120.82.182:9090",
    'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'user-agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
    'cache-control': "no-cache",
    'Accept-Encoding':'gzip, deflate, sdch',
    'Upgrade-Insecure-Requests':'1'
    }



response = requests.get(url, headers=headers, params=querystring)

data = json.loads(response.text)
page = int(data['page']['totalPage'])
print page

headers = {
    'host': "202.120.82.182:9090",
    'accept-encoding': "Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    'cache-control': "no-cache",
    'Cookie':'JSESSIONID=811db904-f275-40f6-877f-c6d22c520a14; rmbUser=true; username=nic; password=nic3081'
    }



for part in range(page/5000-1):
    action = []
    dir = []
    domain = []
    domainname = []
    ipaddr = []
    plat = []
    platformId = []
    referer = []
    rid = []
    sip = []
    starttime = []
    url = []
    websiteId = []
    for p in range(5000*part+1,5000*(part+1)):
        print p
        try:
            data_url = "http://202.120.82.182:9090/currentURL/rtlList"
            querystring = {"limit":"100","page":str(p),"stime":"2017-10-21","etime":"2017-10-21","sip":"","dip":"","platformId":"","websiteId":"","username":"","domain":"","url":"","action":"","platform":"","browser":"","line":"","dir":"","initParam":""}
            response = requests.get(data_url, headers=headers,params=querystring)
            data = json.loads(response.text)['page']['list']
            for item in data:
                action.append(item['action'])
                # print action
                dir.append(item['dir'])
                domain.append(item['domain'])
                domainname.append(item['domainname'])
                ipaddr.append(item['ipaddr'])
                plat.append(item['plat'])
                platformId.append(item['platformId'])
                referer.append(item['referer'])
                rid.append(item['rid'])
                sip.append(item['sip'])
                starttime.append(item['starttime'])
                url.append(item['url'])
                websiteId.append(item['websiteId'])
        except:
            data_url = "http://202.120.82.182:9090/currentURL/rtlList"
            querystring = {"limit":"100","page":str(p),"stime":"2017-10-21","etime":"2017-10-21","sip":"","dip":"","platformId":"","websiteId":"","username":"","domain":"","url":"","action":"","platform":"","browser":"","line":"","dir":"","initParam":""}
            response = requests.get(data_url, headers=headers,params=querystring)
            data = json.loads(response.text)['page']['list']
            for item in data:
                action.append(item['action'])
                # print action
                dir.append(item['dir'])
                domain.append(item['domain'])
                domainname.append(item['domainname'])
                ipaddr.append(item['ipaddr'])
                plat.append(item['plat'])
                platformId.append(item['platformId'])
                referer.append(item['referer'])
                rid.append(item['rid'])
                sip.append(item['sip'])
                starttime.append(item['starttime'])
                url.append(item['url'])
                websiteId.append(item['websiteId'])
    df = DataFrame({'action':action,'dir':dir,'domain':domain,'domainname':domainname,'ipaddr':ipaddr,'plat':plat,'platformId':platformId,'referer':referer,'rid':rid,'sip':sip,'starttime':starttime,'url':url,'websiteId':websiteId})
    df.to_csv(u'2017年10月21日数据part%s.csv'%str(part),encoding='gbk',index=False)


# 最后一部分
action = []
dir = []
domain = []
domainname = []
ipaddr = []
plat = []
platformId = []
referer = []
rid = []
sip = []
starttime = []
url = []
websiteId = []

for p in range(page/5000*5000,page):
    print p
    try:
        data_url = "http://202.120.82.182:9090/currentURL/rtlList"
        querystring = {"limit":"100","page":str(p),"stime":"2017-10-21","etime":"2017-10-21","sip":"","dip":"","platformId":"","websiteId":"","username":"","domain":"","url":"","action":"","platform":"","browser":"","line":"","dir":"","initParam":""}
        response = requests.get(data_url, headers=headers,params=querystring)
        data = json.loads(response.text)['page']['list']
        for item in data:
            action.append(item['action'])
            # print action
            dir.append(item['dir'])
            domain.append(item['domain'])
            domainname.append(item['domainname'])
            ipaddr.append(item['ipaddr'])
            plat.append(item['plat'])
            platformId.append(item['platformId'])
            referer.append(item['referer'])
            rid.append(item['rid'])
            sip.append(item['sip'])
            starttime.append(item['starttime'])
            url.append(item['url'])
            websiteId.append(item['websiteId'])
    except:
        data_url = "http://202.120.82.182:9090/currentURL/rtlList"
        querystring = {"limit":"100","page":str(p),"stime":"2017-10-21","etime":"2017-10-21","sip":"","dip":"","platformId":"","websiteId":"","username":"","domain":"","url":"","action":"","platform":"","browser":"","line":"","dir":"","initParam":""}
        response = requests.get(data_url, headers=headers,params=querystring)
        data = json.loads(response.text)['page']['list']
        for item in data:
            action.append(item['action'])
            # print action
            dir.append(item['dir'])
            domain.append(item['domain'])
            domainname.append(item['domainname'])
            ipaddr.append(item['ipaddr'])
            plat.append(item['plat'])
            platformId.append(item['platformId'])
            referer.append(item['referer'])
            rid.append(item['rid'])
            sip.append(item['sip'])
            starttime.append(item['starttime'])
            url.append(item['url'])
            websiteId.append(item['websiteId'])
df = DataFrame({'action':action,'dir':dir,'domain':domain,'domainname':domainname,'ipaddr':ipaddr,'plat':plat,'platformId':platformId,'referer':referer,'rid':rid,'sip':sip,'starttime':starttime,'url':url,'websiteId':websiteId})
df.to_csv(u'2017年10月21日数据last_part.csv',encoding='gbk',index=False)
      # with codecs.open(u'2017年10月20日数据.csv','a+','utf-8_sig') as f:
        #     writer = csv.DictWriter(f, fieldnames=[])
e = time.clock()
print e-s
print 'welldone'
