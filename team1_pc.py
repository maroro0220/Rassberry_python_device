from socket import *
from time import localtime,strftime
import pccon
class PC:
    def __init__(self):
        self.PORT=50007
        self.s=socket(AF_INET,SOCK_STREAM)
        HOST='192.168.101.120'
        self.s.bind((HOST,self.PORT))
        self.pc=pccon.Pcon()

    def Preceive(self):
        while True:
              self.s.listen(1)
              conn, addr=self.s.accept()
              self.conn=conn
              self.addr=addr
              print('\nConnected by',self.addr)
              while True:
                    data= self.conn.recv(1024)
                    data=data.decode('ascii')
                    if not data: break

                    else:
                        data=tuple(data.split('/'))
                        print(data)
                        self.pc.dbin(data)
                        #self.pc.dipin(data)



        #conn.close()

if __name__=='__main__':
      pc=PC()
#      msg='self.rl.led_on(15)'
      pc.Preceive()
      #pc.Psend(msg)
