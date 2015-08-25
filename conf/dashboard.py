#-*-coding:utf8-*-
import os
 
#-- dashboard db config --
DASHBOARD_DB_HOST = "mysql"
DASHBOARD_DB_PORT = 3306
DASHBOARD_DB_USER = "root"
DASHBOARD_DB_PASSWD = "password"
DASHBOARD_DB_NAME = "dashboard"
 
#-- graph db config --
GRAPH_DB_HOST = "mysql"
GRAPH_DB_PORT = 3306
GRAPH_DB_USER = "root"
GRAPH_DB_PASSWD = "password"
GRAPH_DB_NAME = "graph"
 
#-- app config --
DEBUG = True
SECRET_KEY = "2mf09vjRDC"
SESSION_COOKIE_NAME = "open-falcon"
PERMANENT_SESSION_LIFETIME = 3600 * 24 * 30
SITE_COOKIE = "open-falcon-ck"
 
#-- query config --
QUERY_ADDR = "http://query:9966"
 
BASE_DIR = "/home/dashboard/"
LOG_PATH = os.path.join(BASE_DIR,"log/")
 
try:
    from rrd.local_config import *
except:
    pass

