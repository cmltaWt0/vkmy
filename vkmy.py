#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vkontakte
import sys
import ConfigParser

def config():
    conf = {}
    config = ConfigParser.ConfigParser()
    config.read('conf.cfg')

    conf ['app_id'] = config.get('app', 'app_id')
    conf ['app_secret'] = config.get('app', 'app_secret')

    return conf

conf = config()

app_id = conf['app_id']
app_secret = conf['app_secret']

vk = vkontakte.API(app_id, app_secret)
print vk.getServerTime()
