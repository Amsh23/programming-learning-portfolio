import os
contacts={}
class contact:
    def __init__(self,number,firstname,lastname,address):
        self.number=number
        self.firstname=firstname
        self.lastname=lastname
        self.address=address

def add_number():
    os.system('cls')
    number=input("Enter phonenumber:")
    if number in contacts:
        input("Contact already exists.")
    else:
        firstname=input("Enter first name:")
        lastname=input("Enter last name:")
        address=input("Enter address:")
     
        contacts[number]=contact(number,firstname,lastname,address)
        input("Contact added successfully.")
def delete_number():
    os.system('cls')
    number=input("Enter phonenumber to delete:")
    if number in contacts:
        del contacts[number]
        input("Contact deleted successfully.")
    else:
        input("Contact not found.") 

def update_number():
    os.system('cls')
    number=input("Enter phonenumber to update:")
    if number in contacts:
        firstname=input("Enter new first name:")
        lastname=input("Enter new last name:")
        address=input("Enter new address:")
     
        contacts[number]=contact(number,firstname,lastname,address)
        input("Contact updated successfully.")
    else:
        input("Contact not found.")




def display_menu():
    print("welcome")
    print("-------------------------------------")
    print("1.ADD")
    print("2.DELETE")
    print("3.UPDATE")
    print("4.FIND")
    print("5.DISPLAY")
    print("6.EXIT")
while True:
    display_menu()
    option=input("Enter your choice between 1-6:")  
    if option=="1":
        add_number()
    elif option=="2":
        delete_number()  
    elif option=="3":
        update_number()
    elif option=="4":
        pass
    elif option=="5":
        pass
    elif option=="6":
        break