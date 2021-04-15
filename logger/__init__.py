#-*- coding: utf-8 -*-
import os.path
from .settings import DATABASE_PATH
from .logger import Logger

if not os.path.isfile(DATABASE_PATH):
    from .models import Base, engine
    Base.metadata.create_all(engine)
