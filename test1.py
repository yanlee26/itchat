#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

from itchat.content import *
import requests
import json
import itchat
itchat.auto_login(hotReload = True)
# 调用图灵机器人的api，采用爬虫的原理，根据聊天消息返回回复内容
def tuling(info):
  appkey = "8e1589f7d4b14d7da0cdcbc970262db5"
  url = "http://www.tuling123.com/openapi/api?key=%s&info=%s"%(appkey,info)
  req = requests.get(url)
  content = req.text
  data = json.loads(content)
  answer = data['text']
  return answer
# 对于群聊信息，定义获取想要针对某个群进行机器人回复的群ID函数
def group_id(name):
  df = itchat.search_chatrooms(name=name)
  print(df)
  return df[0]['UserName']

# 注册文本消息，绑定到text_reply处理函数
# text_reply msg_files可以处理好友之间的聊天回复
@itchat.msg_register([TEXT,MAP,CARD,NOTE,SHARING])
def text_reply(msg):
  itchat.send('%s' % tuling(msg['Text']),msg['FromUserName'])
@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
  msg['Text'](msg['FileName'])
  return '@%s@%s' % ({'Picture': 'img', 'Video': 'vid'}.get(msg['Type'], 'fil'), msg['FileName'])
# 现在微信加了好多群，并不想对所有的群都进行设置微信机器人，只针对想要设置的群进行微信机器人，可进行如下设置
@itchat.msg_register(TEXT, isGroupChat=True)
def group_text_reply(msg):
  # 当然如果只想针对@你的人才回复，可以设置if msg['isAt']:
  item = group_id(u'@@7a3dcf6805d672b6f29f76fd9e828fd6c2e2c1e78a12889bdfa369a8634d87c8') # 根据自己的需求设置
  if msg['ToUserName'] == item:
    itchat.send(u'%s' % tuling(msg['Text']), item)

itchat.run()
