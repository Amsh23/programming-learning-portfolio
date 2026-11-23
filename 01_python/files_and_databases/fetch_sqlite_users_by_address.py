import sqlite3
conn=sqlite3.connect(r"C:\Users\Student\Desktop\database1.db")
x=conn.cursor()
x.execute("select * from user where address='tehran'")
rows=x.fetchall()
for row in rows:
    print(row)