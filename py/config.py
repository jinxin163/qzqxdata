# -*- coding:utf-8 -*-
import configparser
import os
from odps import ODPS
from dbClient import mysqlClient

__projectName = 'qzqxdata'
__curPath = os.getcwd()
rootPath = __curPath[:__curPath.find(__projectName) + len(__projectName)]

conf = configparser.ConfigParser()
conf.read(rootPath + r'/conf/conf.ini', encoding='utf-8')

_section1 = 'mysql_conn_zwy'
_section2 = 'odps_conn'

mysqlCli = mysqlClient(host=conf.get(_section1, 'ip'), port=conf.getint(_section1, 'port'),
                       user=conf.get(_section1, 'user'), password=conf.get(_section1, 'pw'),
                       db=conf.get(_section1, 'db'))

odpsCli = ODPS(conf.get(_section2, 'accessId'), conf.get(_section2, 'accessKey'),
               conf.get(_section2, 'project'), endpoint=conf.get(_section2, 'endPoint'))
