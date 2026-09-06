# -*- coding:utf-8 -*-
import os
if os.path.exists(r"C:\Users\Student\Desktop\test.txt"):
    with open(r"C:\Users\Student\Desktop\test.txt","r",encoding="utf-8") as f:

        print(f.read())
else:
    print("not exists")







# f=open(r"C:\Users\Student\Desktop\x.txt",'r')

# with open(r"C:\Users\Student\Desktop\x.txt") as f: