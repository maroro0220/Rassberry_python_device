from socket import *
def client1():
      clientsocket=socket(AF_INET,SOCK_STREAM)
      print('Client :')
      clientsocket.connect(('localhost',8000))
      clientsocket.send('Hello'.encode())
      clientsocket.close()

def client2():
      HOST='localhost'
      PORT=50007
      s=socket(AF_INET,SOCK_STREAM)
      s.connect((HOST,PORT))
      s.sendall('Hello, world'.encode())
      data=s.recv(1024) #buffer가 채워질 때까지 대기 
      s.close()
      print('Received', repr(data))


def client3():
      HOST='localhost'
      PORT=50007
      s=socket(AF_INET,SOCK_STREAM)
      s.connect((HOST,PORT))
      s.sendall('maroro:apple:banana:melon'.encode())       
      #data=s.recv(1)
      #print('Received',repr(data))
      s.close()

      
if __name__=='__main__':
      client3()
