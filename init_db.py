import sqlite3


connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO posts (name1, email) VALUES (?, ?)",
            ('Michael', '@.co.il')
            )

cur.execute("INSERT INTO posts (name1, email) VALUES (?, ?)",
            ('Anat', '@.com')
            )

connection.commit()
connection.close()