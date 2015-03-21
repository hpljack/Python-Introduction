__author__ = 'liuhuiping'

'''''
输入文件名，并且上传
'''

import  socket
import  time
import  struct
import  os

socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) #tcp
socket.timeout(1)
e = 0

try:
    socket.create_connection(('127.0.0.1',8887))
    print('connect')
except socket.timeou:
    print('timeout')
except socket.error:
    print('error')
except e:
    print('any')

if not e:
    while True:
        filename = input('input your filename-------------->')
        FILEINFO_SIZE = struct.calcsize('128sI') #编码格式大小
        fhead = struct.pack('128sI',filename,os.stat(filename).st_size)#按照规则进行打包
        socket.send(fhead)#发��文件基本信息数据
        fp = open(filename,'rb')
        while True:
            filedata = fp.read(1024)
            if not filedata:
                break
            socket.send(filedata)
        print('sending over')
        fp.close()
