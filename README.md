# Python logger module
This module is able to put log messages into stdout, save them in a database, receive logs from a third-party site, sort them and save them to the database.

### Installation
```bash
$ git clone https://github.com/rabarbra/logs_loader
$ cd logs_loader
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

### Usage
```python
from logger import Logger

log_worker = Logger()
```

### Settings
Settings are stored in logger/settings.py file.
* LOGS_URL = "http://www.dsdev.tech/logs/"
Logs api address for Logger.get_logs() method.
* USER_ID = ''
Your user.id in the database
* HOSTNAME = ''
Your hostname
* DATABASE_PATH = 'test.db'
Path to the sqlite database file
* WRITE_TO_STDOUT = True
If True will write logs to stdout while Logger.log()
* WRITE_TO_DB = False
If True will save logs to the database while Logger.log()
* EXCEPTIONS_LOGGING = True
If True will logg exceptions occuried
