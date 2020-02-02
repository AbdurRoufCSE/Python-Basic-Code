mark=float(input("Enter the mark:"))
if mark>=80 and mark<=100:
    print("A+")
elif mark>=70 and mark<=79.9:
    print("A")
elif mark>=60 and mark<=69.9:
    print("A-")
elif mark>=50 and mark<=59.9:
    print("B")
elif mark>=40 and mark<=49.9:
    print("C")
elif mark>=33 and mark<=39.9:
    print("D")
elif mark>=1 and mark<=32.9:
    print("F")