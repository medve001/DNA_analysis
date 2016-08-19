'''
Iserting data into SQLite3 database from csv file
http://stackoverflow.com/questions/2887878/importing-a-csv-file-into-a-sqlite3-database-table-using-python
'''

import csv, sqlite3

conn = sqlite3.connect("res-db.sqlite")
cur = conn.cursor()
cur.execute('CREATE TABLE IF NOT EXISTS restrict(name TEXT, seq TEXT, cut TEXT, size TEXT);')
conn.commit()

with open('res-db.csv','r') as file:
    # csv.DictReader uses first line in file for column headings by default
    dr = csv.DictReader(file) # comma is default delimiter
    to_db = [(i['name'], i['seq'],i['cut'],i['size'], ) for i in dr]

cur.executemany("INSERT INTO restrict (name, seq, cut, size) VALUES (?, ?, ?, ?);", to_db)
conn.commit()
conn.close()
