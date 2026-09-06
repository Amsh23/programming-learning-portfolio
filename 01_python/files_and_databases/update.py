import sqlite3
conn=sqlite3.connect(r"C:\Users\Student\Desktop\database1.db")
x=conn.cursor()
x.execute("update user set address='alborz' where address='karaj'")
conn.commit()
conn.close()