from socket import *
from time import localtime,strftime
class PC:
    def __init__(self):
        self.PORT=50010
        self.s=socket(AF_INET,SOCK_STREAM)
        self.HOST='192.168.101.101'
        self.s.connect((self.HOST,self.PORT))

    def Psend(self,msg):

        self.s.send(msg.encode('ascii'))
        #self.s.close()
        #print(repr(data.decode('ascii')),end='')
        #conn.sendall('self.rl.led_on(15)'.encode('ascii'))

#if __name__=='__main__':
#      pc=PC()
#      msg='l1_on'
      #pc.Preceive()
#      pc.Psend(msg)
