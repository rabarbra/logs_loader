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

#Creating object for logs handling
log_worker = Logger()

#Log message:
log_worker.logg("Message to log")

#Getting data from URL (default: settings.LOGS_URL) with PARAMS.
#Saving data in log_handler.logs
data = log_handler.get_data(PARAMS, URL)

#Sorting data by key (default: 'created_at'). This method changes log_handler.logs
log_handler.sort_data('created_at')

#Saving data to database:
log_handler.save_to_db()
```

### Settings
Settings are stored in logger/settings.py file.
```python
LOGS_URL = "http://www.dsdev.tech/logs/"
#Logs api address for Logger.get_logs() method.
USER_ID = ''
#Your user.id in the database
HOSTNAME = ''
#Your hostname
DATABASE_PATH = 'test.db'
#Path to the sqlite database file
WRITE_TO_STDOUT = True
#If True will write logs to stdout while Logger.log()
WRITE_TO_DB = False
#If True will save logs to the database while Logger.log()
EXCEPTIONS_LOGGING = True
#If True will logg exceptions occuried
```
