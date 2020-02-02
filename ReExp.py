import re
pattern=r"color"

'''if re.match(pattern,"color is color I love Red color"):
    print("Match")
else:
    print("Not match")
'''

'''if re.search(pattern,"Red is color I love Red color"):
    print("Match")
else:
    print("Not match")
'''
if re.findall(pattern,"Red is color I love Red color"):
    print("Match")
else:
    print("Not match")

