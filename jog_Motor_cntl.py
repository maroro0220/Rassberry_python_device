import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#gpio [up, dn, lt, rt, cen]
gpio=[ 5,  6,  16, 20, 21]
#stat [up, dn, lt, rt, cen]
stat =[0,  0,  0,  0,  0]

GPIO.setwarnings(False)
GPIO_RP=4
GPIO_RN=25
GPIO_EN=12

class MOTOR:
    def __init__(self):
      print('init')
      GPIO.setup(GPIO_RP,GPIO.OUT)
      GPIO.setup(GPIO_RN,GPIO.OUT)
      GPIO.setup(GPIO_EN,GPIO.OUT)
      GPIO.output(GPIO_EN,True)
      
    def motor_forward(self):
      print('forword')
      GPIO.output(GPIO_RP,True)
      GPIO.output(GPIO_RN,False)
    def motor_backward(self):
      print('backword')
      GPIO.output(GPIO_RP,False)
      GPIO.output(GPIO_RN,True)
    def motor_stop(self):
      print('stop')
      GPIO.output(GPIO_RP,False)
      GPIO.output(GPIO_RN,False)
      GPIO.output(GPIO_EN,False)
      
    def motor_change_speed(self,p, duty):
      p.ChangeDutyCycle(duty)
    

class CNTL:
    def __init__(self):
        self.m=MOTOR()
        self.m_speed=0
        self.p=GPIO.PWM(GPIO_EN,100)
        self.p.start(0)
    def jog(self):
      try:
          for i in range(5):
                  GPIO.setup(gpio[i],GPIO.IN)
      
          while True:
                if GPIO.input(gpio[0]):
                    self.m_speed+=5
                    if self.m_speed>100:
                        self.m_speed=100
                    self.m.motor_change_speed(self.p, self.m_speed)
                    time.sleep(0.2)
                elif GPIO.input(gpio[1]):
                    self.m_speed-=5
                    if self.m_speed<0:
                        self.m_speed=0
                    self.m.motor_change_speed(self.p, self.m_speed)
                    time.sleep(0.2)
                elif GPIO.input(gpio[2]):
                    time.sleep(0.2)
                    if self.m_speed == 0:
                        self.p.start(100)
                        self.m_speed=100
                    self.m.motor_forward()
                        
                elif GPIO.input(gpio[3]):
                    if self.m_speed == 0:
                        self.p.start(100)
                        self.m_speed=100
                    self.m.motor_backward()
                      
                elif GPIO.input(gpio[4]):
                    self.m.motor_stop()
                    self.m_speed=0
                    time.sleep(0.2)

    
      finally:
            print("Cleaning up")
            GPIO.cleanup()

            
if __name__=='__main__':
      
      c=CNTL()
      c.jog()
