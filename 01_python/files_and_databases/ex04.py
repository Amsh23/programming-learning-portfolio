import sqlite3
conn=sqlite3.connect(r"C:\Users\Student\Desktop\database1.db")
x=conn.cursor()
x.execute("create table if not exists user(ID text primary key,FirstName text,LastName char(20),Age int,Address text,Average real)")
conn.commit()
conn.close()
