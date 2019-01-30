#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-

import itchat, time
from itchat.content import *

@itchat.msg_register([TEXT, MAP, CARD, NOTE, SHARING])
def text_reply(msg):
    # author=itchat.search_friends(nickName='super_6')[0]
    # author.send(msg.text)
    msg.user.send('%s: %s' % (msg.type, msg.text))

@itchat.msg_register([PICTURE, RECORDING, ATTACHMENT, VIDEO])
def download_files(msg):
    msg.download(msg.fileName)
    typeSymbol = {
        PICTURE: 'img',
        VIDEO: 'vid', }.get(msg.type, 'fil')
    return '@%s@%s' % (typeSymbol, msg.fileName)

@itchat.msg_register(FRIENDS)
def add_friend(msg):
    msg.user.verify()
    msg.user.send('Nice to meet you!')

# 发送群聊
@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def group_text_reply(msg):
  group_name = msg['User']['NickName']
# group = ['吃饭', 'itchat','上海','小程序小分队']
# chartrooms = itchat.get_chatrooms()
# print(chartrooms)
# for room in chartrooms:
  print(group_name)
  # itchat.send('text...', toUserName='上海')
    # igroup_info = itchat.search_chatrooms(name=name)
    # item = group_info[0]['UserName']
    # if group_name in group:
    #   itchat.send(get_answer(msg['Text']))

itchat.auto_login(True)
itchat.run(True)
