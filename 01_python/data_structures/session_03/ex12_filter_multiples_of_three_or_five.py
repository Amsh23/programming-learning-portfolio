list=input("enter number ").split()
for i in list:
    if int(i)%3==0 or int(i)%5==0:
        print (i)