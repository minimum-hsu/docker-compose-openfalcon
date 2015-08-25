# -*- coding:utf-8 -*-
 
# -- app config --
DEBUG = False
 
# -- db config --
DB_HOST = "mysql"
DB_PORT = 3306
DB_USER = "root"
DB_PASS = "password"
DB_NAME = "falcon_links"
 
# -- cookie config --
SECRET_KEY = "mfiovn2FfA1yhb"
SESSION_COOKIE_NAME = "falcon-links"
PERMANENT_SESSION_LIFETIME = 3600 * 24 * 30
 
try:
    from frame.local_config import *
except Exception, e:
    print "[warning] %s" % e
