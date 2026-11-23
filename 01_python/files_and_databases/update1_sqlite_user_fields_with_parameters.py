import sqlite3
conn=sqlite3.connect(r"C:\Users\Student\Desktop\database1.db")
x=conn.cursor()
x.execute("update user set address='alborz' where address='karaj'")
x.execute("update user set name=?,address=?,age=? where id=?",('mohsen','tehran',36,'001'))
conn.commit()
conn.close()