#-*- coding: utf-8 -*-
LOGS_URL = "http://www.dsdev.tech/logs/"
USER_ID = ''
HOSTNAME = ''
DATABASE_PATH = 'test.db'

if not HOSTNAME:
    from socket import gethostname
    HOSTNAME = gethostname()

