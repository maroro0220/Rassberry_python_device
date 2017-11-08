import smbus2 as smbus
import time

class I2C_BASE:
    def __init__(self):
        self.bus=smbus.SMBus(1)

class FND(I2C_BASE):
    def __init__(self):
        I2C_BASE.__init__(self)
        self.addr=0x20
        self.config_port=0x06
        self.out_port=0x02
            #       0    1   2     3    4    5    6    7    8   9
        self.data=(0xFC,0x60,0xDA,0xF2,0x66,0xB6,0x3E,0xE0,0xFE,0xF6)
             #     seg1   seg2 seg3 seg4 seg5 seg6
        self.digit=(0x7f,0xBF,0xDF,0xEF,0xF7,0xFB)
        self.out_disp=0
    def fnd(self,num):
        try:
            self.bus.write_word_data(self.addr,self.config_port,0x0000)
            out_disp=0x0003
            self.bus.write_word_data(self.addr,self.out_port,out_disp)
            n1=int(num%10)
            n2=int((num/10)%10)
            n3=int((num/100)%10)
            n4=int((num/1000)%10)
            n5=int((num/10000)%10)
            n6=int((num/100000)%10)
            while True:
                if num!=0:
                    out_disp=self.data[n1]<<8 | self.digit[5]
                    self.bus.write_word_data(self.addr,self.out_port,out_disp)
                    time.sleep(0.00000005)
                if n2!=0:
                    out_disp=self.data[n2]<<8 | self.digit[4]
                    self.bus.write_word_data(self.addr,self.out_port,out_disp)
                    time.sleep(0.00000005)
                if n3!=0:
                    out_disp=self.data[n3]<<8 | self.digit[3]
                    self.bus.write_word_data(self.addr,self.out_port,out_disp)
                    time.sleep(0.00000005)
                if n4!=0:    
                    out_disp=self.data[n4]<<8 | self.digit[2]
                    self.bus.write_word_data(self.addr,self.out_port,out_disp)
                    time.sleep(0.00000005)
                if n5!=0:    
                    out_disp=self.data[n5]<<8 | self.digit[1]
                    self.bus.write_word_data(self.addr,self.out_port,out_disp)
                    time.sleep(0.00000005)
                if n6!=0:    
                    out_disp=self.data[n6]<<8 | self.digit[0]
                    self.bus.write_word_data(self.addr,self.out_port,out_disp)
                    time.sleep(0.00000005)
                #out_disp=self.data[num]<<8 | self.digit[sel+1]
                #self.bus.write_word_data(self.addr,self.out_port,out_disp)
            out_disp=0x0003
            self.bus.write_word_data(self.addr,self.out_port,out_disp)

        except KeyboardInterrupt:
            #out_disp=0x03
            #self.bus.write_word_data(self.addr,self.out_port,out_disp)
            pass
class LIGHT(I2C_BASE):
    def __init__(self):
        I2C_BASE.__init__(self)
        self.addr=0x23   #조도센서 주소
        self.reset=0x07    #pdf 99페이지에서 확인 가능
        self.con_hr_mode=0x10   #이것도 99페이지에서 확인 가능 모드설정. 민감도?

        self.data1=0
        self.data2=0
        self.val=0
        self.light_val=0

    def light(self):
        try:
          self.bus.write_byte(self.addr,self.reset)   #주소, 데이터
          time.sleep(0.05)

          self.bus.write_byte(self.addr,self.con_hr_mode)
          time.sleep(0.2)

          self.data1= self.bus.read_byte(self.addr)  #데이터 읽어오기
          self.data2=self.bus.read_byte(self.addr)
          self.val=(self.data1<<8)|self.data2       #16비트가 상위 하위로 나눠서 들어오기 떄문에  이렇게 함
          self.light_val=self.val/1.2

          print('light_val=%.2f'%self.light_val)
          return self.light_val
        except KeyboardInterrupt:
          #do no anything
            pass
        finally:
            pass
class TEM_HUM(I2C_BASE):
    def __init__(self):
        I2C_BASE.__init__(self)
        self.addr=0x40
        self.cmd_temp=0xf3
        self.cmd_humi=0xf5
        self.soft_reset=0xfe
        self.temp=0.0
        self.humi=0.0
        self.val=0
        self.data=[0,0]
    def tem_hum(self):
        try:
              self.bus.write_byte(self.addr,self.soft_reset)
              time.sleep(0.05)

              #temp
              self.bus.write_byte(self.addr,self.cmd_temp)
              time.sleep(0.26)
              for i in range(0,2,1):
                    self.data[i]=self.bus.read_byte(self.addr)
              self.val=self.data[0]<<8|self.data[1]
              self.temp=-46.85+175.72/65536*self.val
              #hum
              self.bus.write_byte(self.addr,self.cmd_humi)
              time.sleep(0.26)
              for i in range(0,2,1):
                    self.data[i]=self.bus.read_byte(self.addr)
              self.val=self.data[0]<<8|self.data[1]
              self.humi=-6.0+125.0/65536*self.val
              print('temp: %.2f, humi: %.2f'%(self.temp,self.humi))
              return self.temp, self.humi
        except KeyboardInterrupt:
              pass


if __name__=='__main__':
    f=FND()
    lig=LIGHT()
    t_h=TEM_HUM()
#    lig.light()
 #   f.fnd(123456)
    th=t_h.tem_hum()
    
    f.fnd(123456)
