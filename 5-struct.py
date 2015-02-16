__author__ = 'liuhuiping'


if __name__ == '__main__':
    # list
    str = 'dsa54354sdsad908jkldsajfdsafdsadsjkldjlskadsads'
    ls = []
    for i in range(2 ,20,3):
        ls.append(str[i:i+3])
    print(ls)
    # append
    ls.append('Helloword')
    ls.extend('@')
    print(ls)

    lp = ['good']
    lp.extend(ls)
    print(lp)

    ls.insert(0,'who')
    print(ls)
    ls.remove('@')
    print(ls)
    print(ls.pop())
    print(ls.count('who')) # count the who in the list
    print(len(ls))
    print(ls.index('who'))
    ls.sort()
    print(ls)
    ls.reverse()
    print(ls)