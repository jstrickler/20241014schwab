import sqlite3

conn = None

try:
    conn = sqlite3.connect('DATA/presidents.db')
except sqlite3.Error as err:
    print(err)
    exit()
else:
    cursor = conn.cursor()
    cursor.execute("select lastname, party from presidents")
    for row in cursor.fetchall():
        print(row)
finally:
    print("in finally")
    if conn:
        print("closing connection")
        conn.close()
