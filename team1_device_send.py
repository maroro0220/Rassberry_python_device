from socket import *
import Ras_module as r
from time import localtime,strftime
class Device:
    def __init__(self):
        self.PORT=50007
        self.s=socket(AF_INET,SOCK_STREAM)
        self.rl=r.LED()
        self.HOST='192.168.101.120'
        self.s.connect((self.HOST,self.PORT))

    def Dsend(self,inform):
            self.s.send(inform.encode('ascii'))


            print('data: ',inform,'\nsend to ',self.HOST,'success')

if __name__=='__main__':
    dev=Device()
    LED='LED/'+ strftime("%Y-%m-%d %I:%M:%S",localtime())+','+ 'LED1_ON,'+'LED2_OFF'
    dev.Dsend(LED)
