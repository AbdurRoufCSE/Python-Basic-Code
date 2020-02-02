number=0
word=0
letter=0
text=input("Enter any word letter digit:")
for x in range(text):

    if x>='a' and x<='z':
       letter=letter+1


    elif x>='0' and x <='9':
        number=number+1
    elif x==' ':
        word=word+1
print(letter)
print(number)
print(word+1)
