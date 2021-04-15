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
