salary=int(input("enter a number"))
if salary>=40000000:
    salary=0.8*salary
elif 20000000<=salary<40000000:
    salary=salary*0.9
else:
    pass
print(salary)