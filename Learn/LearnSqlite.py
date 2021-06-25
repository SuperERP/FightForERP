import sqlite3
conn = sqlite3.connect('mrsoft.db')



cursor = conn.cursor()
cursor.close()


conn.close()