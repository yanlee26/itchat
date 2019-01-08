#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
from random import randint
import itchat
replies=['Yeah!','OK!','Obviously!','Ofcourse you are!','Fuck!','Shit','Rubbish!','Aha!','idiot!','What?','Not really!','Amazing!','Sounds good!','Perfect!','Never!']
@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    replies.append(msg.text + ',')
    index = randint(0, len(replies))
    text = replies[index]
    return text

itchat.auto_login()
itchat.run()
