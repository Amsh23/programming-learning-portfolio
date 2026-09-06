a = input("enter byour word: ")
count=0
vowel="OoUuEeAaIi"
for i in a:
    if i in vowel:
        count=count+1
print(count)
