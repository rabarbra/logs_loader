#-*- coding: utf-8 -*-
from datetime import date
from pprint import pprint
from get_logs.models import Log

d = date(2021, 1, 22)
Log.load_logs(d)
