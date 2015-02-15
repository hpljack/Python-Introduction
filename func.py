__author__ = 'liuhuiping'

def printHex(x):
    result = ''
    if x == 0:
        result = '0'
    while (x/2) > 0:
        result = str(x%2) + result.strip()
        x = int(x /2 )
    print('0x',result.strip(),sep='')