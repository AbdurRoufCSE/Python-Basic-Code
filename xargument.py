'''def student(*deatails):
    print(deatails[0])
student(101,"Abdur Rouf",5.00,"Rouf")
student(102,"Betlla",4.50)
student(103,"sorna",4.25)
student(104,"bal",4.00)
'''
def add(*numbers):
    sum=0
    for num in numbers:
        sum = sum + num
    print(sum)
add(10,20)
add(10,20,30)
add(10,20,30,40)
add(10,20,30,40,50)