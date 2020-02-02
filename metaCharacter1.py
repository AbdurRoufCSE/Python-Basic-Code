import re
pattren = r"a{1,3}$"
if re.match(pattren,"aaa"):
    print("Matched")
else:
    print("Not matched")