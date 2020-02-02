def fanc(x):
    return x*x-2*x-3
def bisection(a,b):
    if(fanc(a)*fanc(b)>=0):
        print("No root")
        return
    c=a
    while((b-a)>=0.01):
        c=(a+b)/2
        if(fanc(c)==0.0):
            break
        if (fanc(c)*fanc(a)<0):
            b=c
        else:
            a=c
    print("The Root:","%.4f"%c)
a=2
b=3.2
bisection(a,b)