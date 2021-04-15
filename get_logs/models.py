#-*- coding: utf-8 -*-
import requests
import json
from datetime import datetime
from urllib.parse import urlparse
from sqlalchemy import (
        Column,
        String, Integer, DateTime, Text, ForeignKey,
        create_engine
        )
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from .sorting import merge_sort
from . import settings

engine = create_engine("sqlite:///" + settings.DATABASE_PATH)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Log(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key = True)
    created_at = Column(DateTime, default=datetime.utcnow())
    message = Column(Text)
    hostname = Column(String)
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    user = relationship('User')
    
    def __init__(self, message, hostname=settings.HOSTNAME,
                 created_at=datetime.utcnow(), user_id=settings.USER_ID):
        self.message = message
        self.hostname = hostname
        self.created_at = created_at
        if user_id:
            self.user_id = user_id

    def load_logs(date, url=settings.LOGS_URL):
        try:
            host = urlparse(url).netloc
            resp = requests.get(url + date.strftime('%Y%m%d'))
            data = json.loads(resp.text)
            if data['error']:
                raise Exception(data['error'])
            logs = data['logs']
            merge_sort(logs)
            for log in logs:
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
            session.add(Log("Exception occured while Log.load_logs() method: " + str(e)))
            raise
        else:
            session.add(Log(f"Log.load_logs() method succesfully executed. "
                            f"Received {len(logs)} records."))
        finally:
            session.commit()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key = True)
    first_name = Column(String)
    second_name = Column(String)

    def __init__(self, user_id, first_name, second_name):
        self.id = user_id
        self.first_name = first_name
        self.second_name = second_name
