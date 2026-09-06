import string
username = input("Username: ")
password = input("Password: ")

if len(username) < 3 or "@" not in username:
  print("Invalid username")
else:
  print("Valid username")

if len(password) > 8:
  print("Invalid password")
else:
    has_lower = any(ch.islower() for ch in password)
    has_upper = any(ch.isupper() for ch in password)
    has_digit = any(ch.isdigit() for ch in password)
    has_special = any(ch in string.punctuation for ch in password)

if has_lower and has_upper and has_digit and has_special:
  print("Valid password")
else:
  print("Invalid password")



