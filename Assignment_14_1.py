import sqlite3

conn = sqlite3.connect('Ages.sqlite3')
cur = conn.cursor()

# cur.execute('''CREATE TABLE Ages (name VARCHAR(128), age INTEGER)''')
cur.execute('''DELETE FROM Ages''')
cur.execute('''INSERT INTO Ages (name, age) VALUES ('Abi', 28)''')
cur.execute('''INSERT INTO Ages (name, age) VALUES ('Aaron', 27)''')
cur.execute('''INSERT INTO Ages (name, age) VALUES ('Bekim', 16)''')
cur.execute('''INSERT INTO Ages (name, age) VALUES ('Pia', 30)''')
cur.execute('''INSERT INTO Ages (name, age) VALUES ('Mutinta', 36)''')
conn.commit()

cur.execute('''SELECT hex(name || age) AS X FROM Ages ORDER BY X''')

for row in cur :
    print row

cur.close()
