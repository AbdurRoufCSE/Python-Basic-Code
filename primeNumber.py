n=int(input("Enter the integer number:"))
count=0
for i in range(2,n,1):
    if n%i==0:
        count=count+1
        break
if count==0:
    print(n,"is prime number")
else:
    print(n,"is not prime number")