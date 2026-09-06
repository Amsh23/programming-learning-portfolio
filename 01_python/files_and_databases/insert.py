import sqlite3
conn=sqlite3.connect(r"C:\Users\Student\Desktop\database1.db")
x=conn.cursor()
x.execute("insert into user values('001','sara','rad',23,'tehran',11.46)")
conn.commit()
conn.close()