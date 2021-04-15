#-*- coding: utf-8 -*-
import requests
from urllib.parse import urlparse
from datetime import datetime
from . import settings
from .models import Log, User, session
from .sorting import sort

class Logger():
    #Adds new log and saves in self.last_log
    def logg(self, message, hostname=settings.HOSTNAME,
             created_at=datetime.utcnow(), user_id=settings.USER_ID):
        self.last_log = Log(message, hostname, created_at, user_id)
        if settings.WRITE_TO_STDOUT:
            print(str(self.last_log))
        session.add(self.last_log)

    #Gets logs data from url with params, saves in self.logs
    def get_data(self, params, url=settings.LOGS_URL):
        self.url = url + params
        try:
            data = requests.get(self.url).json()
            if data['error']:
                raise Exception(data['error'])
            self.logs = data['logs']
        except Exception as e:
            self.logg("Exception occuried while Logger.get_data(): " + str(e))
            raise
        else:
            self.logg(f"Logger.get_data() executed succesfully. "
                      f"Received {len(self.logs)} records.")
            return self.logs

    #Sorts self.logs by key
    def sort_data(self, key = 'created_at'):
        try:
            self.logs = sort(self.logs, key)
        except AttributeError as e:
            if settings.EXCEPTIONS_LOGGING:
                self.logg("Exception occured while Logger.sort_data(): " + str(e))
            raise
    
    #Saves self.logs and all other logs in this session to database
    def save_to_db(self):
        try:
            host = urlparse(self.url).netloc
            for log in self.logs:
                if not session.query(User).filter_by(id=int(log['user_id'])).first():
                    session.add(User(int(log['user_id']),
                                     log['first_name'],
                                     log['second_name']))
                    session.add(Log(log['message'],
                                    host,
                                    datetime.fromisoformat(log['created_at']),
                                    int(log['user_id'])))
                if not session.query(Log).filter_by(
                        message=log['message'],
                        hostname=host,
                        created_at=datetime.fromisoformat(log['created_at']),
                        user_id=int(log['user_id'])).first():
                    session.add(Log(log['message'],
                                    host,
                                    datetime.fromisoformat(log['created_at']),
                                    int(log['user_id'])))
        except Exception as e:
            session.rollback()
            if settings.EXCEPTIONS_LOGGING:
                self.logg("Exception occured while Logger.save_to_db(): " + str(e))
            raise
        finally:
            if settings.WRITE_TO_DB:
                session.commit()
            else:
                session.rollback()
            session.close()
