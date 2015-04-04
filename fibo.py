__author__ = 'liuhuiping'

def fib(n):
    a,b = 0, 1
    while b < n:
        print(b,end=' ')
        a,b = b,a + b
    print()

def fib2(n):
    result = []
    a,b = 0, 1
    while b < n:
        result.append(b)
        a,b = b, a + b
    return result

def maxtwo(x,y,z):
    if(x > y) and (x > z):
        if y > z:
            return x, y
        else:
            return x,z
    else:
        return y, z

