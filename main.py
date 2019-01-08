#!/usr/bin/env python3.7
# -*- coding: utf-8 -*-
import itchat

@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    text = msg.text + ' , Obviously! '
    return text

itchat.auto_login()
itchat.run()
