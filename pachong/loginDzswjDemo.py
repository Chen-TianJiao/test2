# -*- coding:utf-8 -*-
# 登录电子税务局，并获取主页内容
import requests
import os
import re
import datetime
import time



#设置请求头
headers = {'User-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'}
#登录时需要POST的数据
data = {'username':'91340100MA2MQD5Q26',
        'password':'238675f80d58e96aeb8c49edce8663f6',
        'usertype':'pt',
        'yzm':'',
        'validCode':'',
        'execution':'e1s1',
        '_eventId':'submit',
        'lt':''}

#登录时表单提交到的地址（用开发者工具可以看到）
# dzswj_host = 'http://192.168.203.11:8008/'
#dzswj_host = 'http://192.168.31.31:7007/'
dzswj_host = 'http://149.28.226.114/'
login_url = dzswj_host + 'cas/login'
#构造Session
exSession = requests.Session()
#访问登录界面，获取cookie
resp = exSession.get(login_url, headers = headers)
content = str(resp.content.decode('utf-8'))
print("-------------------------------------------------------------------")
print(str(content))
# 设置登录lt
m = re.compile(r'(?<=name="lt" value=").+?(?=" />)',re.S|re.I|re.U)
lts = m.findall(content)
if len(lts) > 0:
        lt = lts[0]
        print(lt)
        data['lt'] = lt
# 模拟登录
resp = exSession.post(login_url, data, headers)
print("-------------------------------------------------------------------")
print(resp.content.decode('utf-8'))
m2 = re.compile(r'(?<=<div id="errorMsg">).+?(?=</div>)',re.S|re.I|re.U)
errorMsg = m2.findall(str(resp.content.decode('utf-8')))
if len(errorMsg) > 0:
        print(errorMsg[0])

#设置响应编码
resp.encoding = 'utf-8'
#登录后才能访问的网页
url = dzswj_host + 'sb/wssb/getQysdsQcList'

#发送访问请求
resp = exSession.get(url)
print("-------------------------------------------------------------------")
print(resp.content.decode('utf-8'))
m = re.compile(r'(?<=onclick="com.login).+?(?=">登录</button>)',re.S|re.I|re.U)
lts = m.findall(str(resp.content.decode('utf-8')))
if len(lts) > 0:
        print('登录失败！')

# 打印申报查询页面内容
#print(resp.content.decode('utf-8'))
# 打印页面返回状态码
#print(resp.status_code)
# 打印响应时间
#print(resp.elapsed.microseconds/1000)
lrrq = datetime.datetime.now()
print('发送时间：' + str(lrrq) + '，响应状态：' + str(resp.status_code) + '，耗时时间：' + str(resp.elapsed.microseconds/1000))
# 十秒执行一次
#time.sleep(10)