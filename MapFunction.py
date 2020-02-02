'''def squere(x):
    return x*x


num = [1,2,3,4,5]
Result=list(map(squere,num))
print(Result)
'''
'''num=[1,2,3,4,5]
result=list(filter(lambda a:a%2==0,num))
print(result)
'''
num=[1,2,3,4,5]
result=[x for x in num if x%2==0 ]
print(result)

result2=[x*x for x in num]
print(result2)