import smbus2 as smbus
import time

bus =smbus.SMBus(1)  #1번포트 쓰겠다
addr=0x23   #조도센서 주소
reset=0x07    #pdf 99페이지에서 확인 가능
con_hr_mode=0x10   #이것도 99페이지에서 확인 가능 모드설정. 민감도?

data1=0
data2=0
val=0
light_val=0

try:
      bus.write_byte(addr,reset)   #주소, 데이터 
      time.sleep(0.05)
      while True:
            bus.write_byte(addr,con_hr_mode)   
            time.sleep(0.2)

            data1= bus.read_byte(addr)  #데이터 읽어오기
            data2=bus.read_byte(addr)
            val=(data1<<8)|data2       #16비트가 상위 하위로 나눠서 들어오기 떄문에  이렇게 함 
            light_val=val/1.2

            print('light_val=%.2f'%light_val)
            time.sleep(1)
except KeyboardInterrupt:
      #do no anything
      pass
finally:
      pass
