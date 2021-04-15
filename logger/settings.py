#-*- coding: utf-8 -*-
#Url for getting logs whith Logger.get_data()
LOGS_URL = "http://www.dsdev.tech/logs/"
#Your user.id in the database
USER_ID = ''
#Your hostname
HOSTNAME = ''
#Path to the database file
DATABASE_PATH = 'test.db'
#If True will write logs to stdout while Logger.log()
WRITE_TO_STDOUT = True
#If True will save logs to the database while Logger.log()
WRITE_TO_DB = False
#If True will logg exceptions occuried
EXCEPTIONS_LOGGING = True

if not HOSTNAME:
    from socket import gethostname
    HOSTNAME = gethostname()

