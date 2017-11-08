import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#gpio [up, dn, lt, rt, cen]
gpio=[ 5,  6,  16, 20, 21]
#stat [up, dn, lt, rt, cen]
stat =[0,  0,  0,  0,  0]

GPIO.setwarnings(False)

class GPIO_BASE:
      def __init__(self):
          self.duty=0
          #GPIO.setup(EN,GPIO.OUT)  #EN
         # GPIO.setup(Led1,GPIO.OUT)  #LED1
          #GPIO.setup(Led2,GPIO.OUT)  #LED2
          self.j=JOG()
      def Change_DutyCycle(self, p, duty):
          p.ChangeDutyCycle(duty)
                  
class MOTOR(GPIO_BASE):
    def __init__(self):
          GPIO_BASE.__init__(self)
          print('init')
          
          self.GPIO_RP=4
          self.GPIO_RN=25
          self.GPIO_EN=12
          
          GPIO.setup(self.GPIO_RP,GPIO.OUT)
          GPIO.setup(self.GPIO_RN,GPIO.OUT)
          GPIO.setup(self.GPIO_EN,GPIO.OUT)
          self.p=GPIO.PWM(12,100)
          self.p.start(0)
          GPIO.output(self.GPIO_EN,True)
          
          
    def motor_forward(self):
          print('forword')
          GPIO.output(self.GPIO_RP,True)
          GPIO.output(self.GPIO_RN,False)
          GPIO.output(self.GPIO_EN,True)
    def motor_backward(self):
          print('backword')
          GPIO.output(self.GPIO_RP,False)
          GPIO.output(self.GPIO_RN,True)
          GPIO.output(self.GPIO_EN,True)
    def motor_stop(self):
          print('stop')
          GPIO.output(self.GPIO_RP,False)
          GPIO.output(self.GPIO_RN,False)
          GPIO.output(self.GPIO_EN,False)
      
    def motor_cntl(self):
          try:
                for i in range(5):
                      GPIO.setup(gpio[i],GPIO.IN)
      
                while True:
                      if GPIO.input(gpio[0]):
                          print('up')
                          self.duty+=5
                          if self.duty>100:
                              self.duty=100
                          super().Change_DutyCycle(self.p, self.duty)
                          self.motor_forward()
                          time.sleep(0.1)
                      elif GPIO.input(gpio[1]):
                            print('down')
                            self.duty-=5
                            if self.duty<0:
                                  self.duty=0
                            super().Change_DutyCycle(self.p, self.duty)
                            self.motor_forward()
                            time.sleep(0.1)
                      elif GPIO.input(gpio[2]):
                            print('left')
                            if self.duty == 0:
                                  self.p.start(100)
                            self.duty=100
                            super().Change_DutyCycle(self.p, self.duty)           
                            self.motor_forward()
                            time.sleep(0.1)
                        
                      elif GPIO.input(gpio[3]):
                            print('right')
                            if self.duty== 0:
                                  self.p.start(100)
                                  self.duty=100
                            self.duty=100
                            super().Change_DutyCycle(self.p, self.duty)   
                            self.motor_backward()
                            time.sleep(0.1)
                      
                      elif GPIO.input(gpio[4]):
                            print('center')
                            self.motor_stop()
                            self.duty=0
                            time.sleep(0.1)
          finally:
                print("Cleaning up")
                GPIO.cleanup()
                  
            

class LED(GPIO_BASE):
      
      def __init__(self):
            GPIO_BASE.__init__(self)
            self.led_pin1=14
            self.led_pin2=15
            self.leds=(self.led_pin1,self.led_pin2)
            print('led_init')

            for i in range(5):
                  GPIO.setup(gpio[i],GPIO.IN)
            for i in self.leds:
                  GPIO.setup(i,GPIO.OUT)
            self.p1=GPIO.PWM(self.led_pin1,100)
            self.p1.start(0)
            self.p2=GPIO.PWM(self.led_pin2,100)
            self.p2.start(0)
      def led_on(self,led_pin ):
            GPIO.output( led_pin, True )
      def led_off(self,led_pin ):
            GPIO.output( led_pin, False )
      def led_cntl(self):
            try:
                  while True:
                        if GPIO.input(gpio[0]):
                              #led1 off led2 on
                              self.duty+=5
                              if self.duty>100:
                                  self.duty=100
                              super().Change_DutyCycle(self.p1,self.duty)
                              super().Change_DutyCycle(self.p2,self.duty)
                              time.sleep(0.1)
                        elif GPIO.input(gpio[1]):
                              #led1 on led2 off
                              self.duty-=5
                              if self.duty<0:
                                  self.duty=0
                              super().Change_DutyCycle(self.p1,self.duty)
                              super().Change_DutyCycle(self.p2,self.duty)
                              time.sleep(0.1)
                        elif GPIO.input(gpio[2]) or GPIO.input(gpio[4]):
                              #leds on
                              self.led_on(self.led_pin1)
                              self.led_on(self.led_pin2)
                              self.duty=100
                              super().Change_DutyCycle(self.p1,self.duty)
                              super().Change_DutyCycle(self.p2,self.duty)
                        elif GPIO.input(gpio[3]):
                              #leds off
                              self.led_off(self.led_pin1)
                              self.led_off(self.led_pin2)
                              self.duty=0
                              super().Change_DutyCycle(self.p1,self.duty)
                              super().Change_DutyCycle(self.p2,self.duty)
            finally:
                  print("Cleaning up")
                  GPIO.cleanup()

class JOG(GPIO_BASE):
      def __init__(self):
            for i in range(5):
                  GPIO.setup(gpio[i],GPIO.IN)
      def jog(self):
            try:
                  while True:
                        if GPIO.input(gpio[0]):
                              #led1 off led2 on
                              self.led_on(self.led_pin1)
                              self.led_off(self.led_pin2)
                        elif GPIO.input(gpio[1]):
                              #led1 on led2 off
                              self.led_on(self.led_pin2)
                              self.led_off(self.led_pin1)
                        elif GPIO.input(gpio[2]) or GPIO.input(gpio[4]):
                              #leds on
                              self.led_on(self.led_pin1)
                              self.led_on(self.led_pin2)
                        elif GPIO.input(gpio[3]):
                              #leds off
                              self.led_off(self.led_pin1)
                              self.led_off(self.led_pin2)
            finally:
                  print("Cleaning up")
                  GPIO.cleanup()
                  
if __name__=='__main__':
      base=GPIO_BASE()
      #ld=LED()
      mt=MOTOR()
      mt.motor_cntl()
      #ld.led_cntl()
