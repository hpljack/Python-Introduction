__author__ = 'liuhuiping'


def fibo(x):
    a,b = 0,1
    while b < x:
        print(b)
        a, b=  b , a + b

if __name__ == '__main__':
    print(2 + 4)
    print(3 / 5)
    print(5 % 9)
    print(8 * 4 - (43 / 5))

    width = 20
    height = 5 * 9
    print(width * height)

    x = y = z = 0
    print(x,y,z,sep='|',end='')
    #float calc
    print(3 * 3.75)

    x = 3 + 5j
    print(x.real)
    print(x.imag)
    print(x)

    # _ means the last calc result
    tax = 12.5/100
    price = 100.50
    print(price * tax)
    # print(price+_)
    # print(round(_,2))

    #string
    hello = 'this is a rather long string contianing\n\serveral lines of text just as you would do in c.\n\ Note that whitespace at the beginning of the lines is\ sigificant'
    print(hello)

    # import printHex from func
    # printHex(3)

    #string tuple
    word = 'Help' + 'A'
    print(word[4])
    print(word[0:2])
    print(word[-2:])
    print(word[1:100])
    print(word[1:])
    print(word[0:])
    print(word[0: -2] + word[-2:] )
    print(word,'len is ',len(word))

    # unicode
    print('Hello\u0020world')
    print('Apfel'.encode('utf-8'))

    #list
    a = ['egg','orange',323,True]
    print(a)
    print(a[0:1])
    print(a[2:3])
    print(a[-2:])
    a.append('nihao')
    print(a)
    for x in range(len(a)):
        print(a[x:x+1])

    while len(a) > 0:
        print(a.pop(),end=',')

    fibo(10)
