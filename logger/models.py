# -*- coding: utf-8 -*-
from sqlalchemy import (
        Column,
        String, Integer, DateTime, Text, ForeignKey,
        create_engine
        )
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from . import settings

engine = create_engine("sqlite:///" + settings.DATABASE_PATH)
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


class Log(Base):
    __tablename__ = 'logs'
    id = Column(Integer, primary_key=True)
    created_at = Column(DateTime, nullable=False)
    message = Column(Text)
    hostname = Column(String(150))
    user_id = Column(Integer, ForeignKey('users.id'), nullable=True)
    user = relationship('User')

    def __init__(self, message, hostname, created_at, user_id):
        self.message = message
        self.hostname = hostname
        self.created_at = created_at
        if user_id:
            self.user_id = user_id

    def __repr__(self):
        return f"{self.__class__.__name__} {str(self.id)}"

    def __str__(self):
        return(f"{self.hostname} {self.created_at} "
               f"{'user: ' + str(self.user_id) if self.user_id else ''}\n"
               f"  {self.message} ")

    def get_all_logs(self):
        return(session.query(Log).all())


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    first_name = Column(String(150))
    second_name = Column(String(150))

    def __init__(self, user_id, first_name, second_name):
        self.id = user_id
        self.first_name = first_name
        self.second_name = second_name

    def __repr__(self):
        return f"{self.__class__.__name__} {str(self.id)}"
