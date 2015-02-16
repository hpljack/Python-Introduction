__author__ = 'liuhuiping'

def isPosOrNag():
    # if elif else sample
    x = int(input('please input an integer: '))
    if x < 0:
        print('Negative changed to zero')
    elif x == 0:
        print('zero')
    else:
        print('postive changed to zero')

def initlog(*args):
        pass

#define function
def ask_ok(prompt,retres= 4,complaint='yes or no,please!'):
    while True:
        ok = input(prompt)
        if ok in ('y','ye','yes'):
            return  True
        if ok in ('n','no','nop','nope'):
            return  False
        retres -= 1
        if retres < 0:
            raise IOError('refusenik user')
    print(complaint)


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")

def cheeseshop(kind,*argments,**keywords):
    print('--Do you have any ',kind, '?')
    print("--I'm sorry, we're all out of ", kind)
    for arg in argments:
        print(arg)
    print('-' * 40)
    keys = sorted(keywords.keys())
    for kw in keys:
        print(kw," : ",keywords[kw])

# changable argments
def write_multiple_items(file,separator,*args):
    file.write(separator.join(args))

def concat(*arg,sep='/'):
    return sep.join(arg)

# lambda expression
def make_increment(n):
    return lambda x : x + n

#document
def my_function():
    """
    Do nothing, but document it ...
    No, Really, it doesn't do anthing...
    """
    pass

if __name__ == '__main__':
    print(concat('dsa','|'))
    #function sample
    # ask_ok('Do you really want to quit? ')

    # isPosOrNag()

    # for sample
    a = ['cat','window',True,4343]
    for x in a:
        print(x)

    #range sample
    for i in range(5,10,2): # range(start,end,step)
        print(i,end=',')
    print()

    for i in range(len(a)):
        print(a[i:i+1],sep=',',end='')

    #pass no nothing
    # while True:
    #     pass
    print()


    parrot(1000)

    cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")

    # list(range())
    print(list(range(3,6)))

    #lambda expression
    f = make_increment(2)
    print(f(3))

    # document
    print(my_function.__doc__)




