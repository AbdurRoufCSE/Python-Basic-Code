import re
pattren =r"colour"
test1="My favourite colour is Red.I love Red colour"
test2=re.sub(pattren,"color",test1)
print(test2)
