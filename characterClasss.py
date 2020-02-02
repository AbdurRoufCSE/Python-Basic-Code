import re
pattren=r"[A-Z][a-z][0-9]"
if re.match(pattren,"Ab1"):
    print("Matched")
else:
    print("Not matched")