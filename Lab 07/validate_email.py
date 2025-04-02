# validate an email address using regex

import re
pattern = "^[a-z 0-9]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
email=input("enter your email:")
if re.search(pattern,email):
    print("valid")
else:
    print("Not valid")
