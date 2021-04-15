#-*- coding: utf-8 -*-
LOGS_URL = "http://www.dsdev.tech/logs/"
USER_ID = ''
HOSTNAME = ''
DATABASE_PATH = 'test.db'
WRITE_TO_STDOUT = True
WRITE_TO_DB = True
EXCEPTIONS_LOGGING = True

if not HOSTNAME:
    from socket import gethostname
    HOSTNAME = gethostname()

