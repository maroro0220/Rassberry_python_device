from socket import *
def server1():
      svrsock=socket(AF_INET,SOCK_STREAM)
      svrsock.bind(('localhost',8000))
      print('Server Info: localhost'+str(8000))
      svrsock.listen(1)
      conn,addr=svrsock.accept()
      print('Client Info:'+addr[0]+':'+str(addr[1]))
      conn.recv(1024)
      conn.close()
def server2():
      HOST='localhost'
      PORT=50007
      s=socket(AF_INET,SOCK_STREAM)
      s.bind((HOST,PORT))
      s.listen(1)
      conn, addr=s.accept()
      print('Connected by',addr)
      while True:
            data= conn.recv(1024)
            if not data: break
            conn.sendall(data)
      conn.close()

def server3():
      HOST='localhost'
      PORT=50007
      s=socket(AF_INET,SOCK_STREAM)
      s.bind((HOST,PORT))
      s.listen(1)
      while True:
            conn, addr=s.accept()
            print('Connected by',addr)
            while True:
                  data= conn.recv(1024)
                  conn.sendall(data)
                  print('Received',repr(data))
                  conn.close()
                  break

def server4():
      HOST='localhost'
      PORT=50007
      s=socket(AF_INET,SOCK_STREAM)
      s.bind((HOST,PORT))

      while True:
            s.listen(1)
            conn, addr=s.accept()
            print('Connected by',addr)
            while True:
                  data= conn.recv(1)
                  if not data:
                        conn.close()
                        break
                  print('Received',repr(data))
            conn.close()
            
def server5():
      HOST='localhost'
      PORT=50007
      s=socket(AF_INET,SOCK_STREAM)
      s.bind((HOST,PORT))

      while True:
            s.listen(1)
            conn, addr=s.accept()
            print('Connected by',addr)
            while True:
                  data= conn.recv(1)
                  if not data: break
                  elif data==b':':print('')
                  else: print(repr(data),end='')
            conn.close()                

if __name__=='__main__':
      server5()
