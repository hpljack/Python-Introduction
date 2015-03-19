__author__ = 'liuhuiping'


import  fibo
if __name__ == '__main__':
    fibo.fib(1000)
    ls = fibo.fib2(100)
    print(ls)

    # import module function
    from fibo import fib,fib2
    from fibo import *



