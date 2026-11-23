user = input("enter your username : ")
password = input("enter your password : ")
if user == "mft" and password == "1234" :
    print("correct!")
elif user != "mft" and password != '1234' :
    print("both are wrong")
elif user != "mft" and password == '1234':
    print("username is incorrect !")
else:
    print("password is incorrect !")
