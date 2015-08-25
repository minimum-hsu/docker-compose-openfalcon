# -*- coding:utf-8 -*-
  
# -- app config --
DEBUG = False
  
# -- db config --
DB_HOST = "mysql"
DB_PORT = 3306
DB_USER = "root"
DB_PASS = "password"
DB_NAME = "falcon_portal"
  
# -- cookie config --
SECRET_KEY = "92j#Ffaas%W"
SESSION_COOKIE_NAME = "falcon-portal"
PERMANENT_SESSION_LIFETIME = 3600 * 24 * 30
  
UIC_ADDRESS = {
    'internal': 'http://192.168.1.100:1234',
    'external': 'http://192.168.1.100:1234',
}
  
UIC_TOKEN = ''
  
MAINTAINERS = ['root']
CONTACT = 'minimum@cepave.com'
  
COMMUNITY = True
  
try:
    from frame.local_config import *
except Exception, e:
    print "[warning] %s" % e
