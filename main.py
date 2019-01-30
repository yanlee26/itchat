#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import itchat
import json
import requests
name='Elliot'

def get_data(text):
    userId = '123456'
    inputText = {'text': text}
    key = '8e1589f7d4b14d7da0cdcbc970262db5'
    userInfo = {'apiKey': key, 'userId': userId}
    perception = {'inputText': inputText}
    data = {'perception': perception, 'userInfo': userInfo}
    return data


def get_answer(text):
    data = get_data(text)
    url = 'http://openapi.tuling123.com/openapi/api/v2'
    response = requests.post(url=url, data=json.dumps(data))
    response.encoding = 'utf-8'
    result = response.json()
    answer = result['results'][0]['values']['text']
    return answer

# 回复好友
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    myself = itchat.get_friends(update=True)[0]['NickName']
    content = msg['Content']
    friend = msg['User']['NickName']
    # 给特定的人的回复，并且自己发的 不回复
    if friend != myself and friend!= 'FRIEND':
        print('%s: %s' % (friend, content))
        answer = get_answer(msg['Text'])
        itchat.send(answer, msg['FromUserName'])
        print('我：%s' % answer)
    else:
        itchat.send('你是猪', msg['FromUserName'])

# @itchat.msg_register(FRIENDS)
# def add_friend(msg):
#     msg.user.verify()
#     msg.user.send('Nice to meet you!')

# 获得群聊ID
def group_id(name):
    df = itchat.search_chatrooms(name=name)
    return df[0]['UserName']

# 发送群聊
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def group_text_reply(msg):
    group_name = msg['User']['NickName']
    group = ['吃饭', 'itchat','上海','小程序小分队',]
    igroup_info = itchat.search_chatrooms(name=name)
    print(igroup_info)
    item = group_info[0]['UserName']
    if group_name in group:
        itchat.send(get_answer(msg['Text']), item)

itchat.auto_login(hotReload=True)
itchat.run()