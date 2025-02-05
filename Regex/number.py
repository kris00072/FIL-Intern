import re

print("Valid" if re.fullmatch(r"^[a-z][^@#$]*\d.*\d.*$", input("Enter email: ")) else "Invalid")
#email
#start with a letter[a-z]