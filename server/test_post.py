"""
Test POST to db.php.

"""
from __future__ import print_function

import datetime
import pytz
import random
import requests
import sqlite3
import sys

if len(sys.argv) < 2:
    print("Pass URL to db.php as first argument")
    sys.exit(1)
else:
    URL = sys.argv[1]

now = datetime.datetime.now()
dt = pytz.utc.localize(now)

data = {
    'session': 'hello',
    'location': '(1,2)',
    # This is the format the SQLite inserts automatically for dt_received.
    # Stored in UTC.
    'dt_sent': now.strftime("%Y-%m-%d %H:%M:%S"),
    'frequency_in': random.randint(0, 100),
    'frequency_out': random.randint(0, 100)
}

x = requests.post(URL, data=data)
print(x.text)

db = sqlite3.connect('frequencies.sqlite3')
c = db.cursor()
c.execute('SELECT * FROM frequencies ORDER BY id DESC LIMIT 1;')
print(c.fetchall())
db.close()

