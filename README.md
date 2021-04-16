# Python logger module
This module allows you to put log messages into stdout, save your owd log messages to the database, receive logs from a third-party site, sort them by key and save them to the database.

### Installation
```bash
$ git clone https://github.com/rabarbra/logs_loader
$ cd logs_loader
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

### Usage
First you need to create a Logger instance. Logger is a singleton class, so it will return you the same instance created at first call every time you want to create new Logger instance. Logger singleton is multithread-safe.
```python
from logger import Logger

# Creating object for logs handling
log_worker = Logger()

# Log message. Log object stores in log_worker.last_log
log_worker.logg("Message to log")

# Getting data from URL (default: settings.LOGS_URL) with PARAMS.
# Saving data in log_handler.logs
data = log_handler.get_data(PARAMS, URL)

# Sorting data by key (default: 'created_at').
# This method changes log_handler.logs
log_handler.sort_data('created_at')

# Saving data to database:
log_handler.save_to_db()

# Get last log message
log_handler.last_log.message

# Get last log hostname
log_handler.last_log.hostname

# Get last log creation date
log_handler.last_log.created_at

# Get last log user id
log_handler.last_log.user_id

# Get all logs stored in the database
all_logs = log_handler.lase_log.get_all_logs()
```

### Settings
Settings are stored in logger/settings.py file.
```python
LOGS_URL = "http://www.dsdev.tech/logs/"
# Logs api address for Logger.get_logs() method.
USER_ID = ''
# Your user.id in the database
HOSTNAME = ''
# Your hostname
DATABASE_PATH = 'test.db'
# Path to the sqlite database file
WRITE_TO_STDOUT = True
# If True will write logs to stdout while Logger.log()
WRITE_TO_DB = False
# If True will save logs to the database while Logger.log()
EXCEPTIONS_LOGGING = True
# If True will logg exceptions occuried
```

### Testing
```bash
$ python -m unittest -v tests/test.py
```
