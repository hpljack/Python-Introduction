__author__ = 'liuhuiping'

if __name__ == '__main__':
    ls = []
    ls.append('didicate')
    ls.insert(0,'halan kailer')
    ls.extend('martin')
    ls.sort()
    print(ls)
    ls.reverse()
    print(ls)
    print(ls.pop())
    print('count the number of d in ls',ls.count('m'))
    print('hello world')

    # use list for stack

    stack = [3,4,5]
    stack.append(6)
    stack.append(7)
    stack.append(8)
    for i in range(len(stack)):
        print(stack.pop())

    #use list for quene
    from collections import deque
    queue = deque(['Erric','debeit','alians'])
    queue.append('Terry')
    queue.append('Grahmad')
    for i in range(len(queue)):
        print(queue.popleft())

    square = []
    for x in range(10):
        square.append(x ** 2)
    for i in range(len(square)):
        print(square.pop())

    