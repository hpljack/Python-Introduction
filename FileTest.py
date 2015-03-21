__author__ = 'liuhuiping'

def LoadF(filename):
    result = []
    with open(filename,"r") as fd:
        i = 4
        for line in fd:
            if len(line) > 0:
                line = line.strip('\n')
                line = line.strip(',')
                lstr = ' ' * 2 + line + ' '* (28 - len(line)) +  '=' + ' ' + str(i) + ';'
                result.append(lstr)
                i += 1
    return  result

def LoadF2(filename):
    result = []
    with open(filename,"r") as fd:
        for line in fd:
            if line.find('//') > 0: #注释行
                result.append(line)
                continue
            else: #非注释行
                ls = line.split(':')
                pos = line.find(':')
                cmdid = line[0:pos - 1]


if __name__ =='__main__':
    # ls = LoadF('test.txt');

    # for l in ls:
    #     print(l)

    line = "QQICON: (sCmd: 'tianyshje'; nPermissionMin: 10; nPermissionMax: 10);"
    pos = line.find(':');
    cmdid = line[0:pos]
    print(cmdid)
    str = line[pos + 2:len(line) - 2]
    print(str)



    print(line)
