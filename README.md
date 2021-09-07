# Python logger module
This module allows you to put log messages into stdout, save your own log messages to the database, receive logs from a third-party site, sort them by key and save them to the database.

---
### Installation
```bash
$ git clone https://github.com/rabarbra/logs_loader
$ cd logs_loader
$ python3 -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
```

---
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
all_logs = log_handler.last_log.get_all_logs()
```

---
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

---
### Testing
```bash
$ python -m unittest -v tests/test.py
```

---
### Additional info

1. Logger.get_data() uses requsts library for sending HTTP requests to server.
2. logger.sorting.sort() uses merge sort algorithm. Worst-case performance of merge sort is O(n log n). The disadvantage is that the algorithm requires O(n) space in worst case. I need to write the realisation with linked lists later to attaim O(1) space complexity.
3. Here is my sqlite3 database schema:
```
table logs
  "id" INTEGER NOT NULL
  "created_at" DATETIME NOT NULL
  "message" TEXT
  "hostname" VARCHAR(150)
  "user_id" INTEGER
table users
  "id" INTEGER NOT NULL
  "first_name" VARCHAR(150)
  "second_name" VARCHAR(150)
```
4. Logger.save_to_db() saves all received logs in database
5. I use python unittest module for testing. To emulate requests.get() method unittest.mock.Mock object is used.
6. All exceptions are logged if settings.EXCEPTIONS_LOGGING is True.
7. Logger.get_data() method is logged.
8. Logger.get_data() method is an entry point.
9. Logger is a singleton class, so it will return you the same instance created at first call every time you want to create new Logger instance. Logger singleton is multithread-safe.
