import sqlite3
conn=sqlite3.connect(r"C:\Users\Student\Desktop\database1.db")
x=conn.cursor()
x.execute("delete from user where name='mohsen'")
conn.commit()
conn.close()