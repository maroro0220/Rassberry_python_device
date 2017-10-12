from socket import *
import team1_GPIO as r
import decon as dcon
from time import localtime,strftime
class Device:
    def __init__(self):
        self.PORT=50010
        self.s=socket(AF_INET,SOCK_STREAM)
        self.rl=r.LED()
        self.HOST='192.168.101.101'
        self.s.bind((self.HOST,self.PORT))
        self.dcon=dcon.DV_Con()

    def Dreceive(self):
        while True:
          self.s.listen(1)
          conn, addr=self.s.accept()
          self.conn=conn
          self.addr=addr
          print('\nConnected by',self.addr)
          while True:
                data= self.conn.recv(1024)
                data=data.decode('ascii')
                self.dcon.conGP(data)
                print(data)
                if data=='00':
                    self.rl.led1_on()
                
                #eval(data.decode('ascii'))
          #conn.close()

if __name__=='__main__':
    dev=Device()
    dev.Dreceive()
