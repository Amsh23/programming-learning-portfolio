dict1={"car":"ماشین","cat":"گربه","home":"خانه","library":"کتابخانه","bus":"اتوبوس","door":"در"}
word=input("enter word=")
if word in dict1.keys():
    print(dict1[word])
else:
    q=input("do you know meaning of this word?").lower()
    if q=="yes":
        answer=input("enter answer=")
        dict1[word]=answer
    else:
        print("bye")
print(dict1)