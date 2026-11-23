name=input("enter name=")
age=int(input('enter age='))
avg=float(input("""enter age="""))
print("my name is ",name,".I\'m ",age," years old,my average is ",round(avg,2))
print(f"my name is {name}.I\'m {age} years old,my average is {avg:.2f}")
print("my name is {}.I\'m {} years old,my average is {:.2f}".format(name,age,avg))
print("my name is %s.I\'m %d years old,my average is %.2f"%(name,age,avg))





