#!/usr/bin/env python
# -*- coding: utf-8 -*-

import vkontakte
from ConfigParser import ConfigParser

config = ConfigParser()
config.read('conf.cfg')

app_id = config.get('app', 'app_id')
app_secret = config.get('app', 'app_secret')

vk = vkontakte.API(app_id, app_secret)
print vk.getServerTime()
