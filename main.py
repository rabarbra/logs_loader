#-*- coding: utf-8 -*-
from datetime import date
from pprint import pprint
from logger.logger import Logger
from logger import settings

def main():
    d = date(2021, 1, 22)
    PARAMS = d.strftime('%Y%m%d')
    URL = settings.LOGS_URL

    #Creating object for logs handling
    log_handler = Logger()

    #Getting data from URL (default: settings.LOGS_URL) with PARAMS.
    #Saving data in log_handler.logs
    data = log_handler.get_data(PARAMS, URL)

    #Sorting data by key (default: 'created_at'). This method changes log_handler.logs
    log_handler.sort_data('created_at')

    #Saving data to database:
    log_handler.save_to_db()

if __name__ == '__main__':
    main()
