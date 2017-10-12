import RPi.GPIO as GPIO
import time


class GPIO_BASE:
      def __init__(self):

          GPIO.setmode(GPIO.BCM)
          GPIO.setwarnings(False)
          self.duty=0
          #GPIO.setup(EN,GPIO.OUT)  #EN
         # GPIO.setup(Led1,GPIO.OUT)  #LED1
          #GPIO.setup(Led2,GPIO.OUT)  #LED2

      def Change_DutyCycle(self, p, duty):
          p.ChangeDutyCycle(duty)
class PIEZO(GPIO_BASE):
      def __init__(self):
            GPIO_BASE.__init__(self)
            self.gpio_pin=13
            self.scale=[261,294,329,349,392,440,493,523]
            GPIO.setup(self.gpio_pin,GPIO.OUT)
            self.p=GPIO.PWM(self.gpio_pin,100)
      def piezo(self):
            #try:
                  self.p=GPIO.PWM(self.gpio_pin,100)
                  self.p.start(100)     #start the PWM on 100% duty cycle
                  self.p.ChangeDutyCycle(90)   #change the duty cycle to 90%

                  for i in range(8):
                        print(i+1)
                        self.p.ChangeFrequency(self.scale[i])
                        time.sleep(1)
                  self.p.stop()      #stop the PWM output

            #finally:
            #    print("finish")
                  #GPIO.cleanup()

class UltSon(GPIO_BASE):
      def __init__(self):
            GPIO_BASE.__init__(self)
            self.trig=0
            self.echo=1

            GPIO.setup(self.trig,GPIO.OUT)
            GPIO.setup(self.echo,GPIO.IN)  #Peri v2.1
      def ultson(self):
            try:
                  while True:
                        GPIO.output(self.trig,False)
                        time.sleep(0.5)

                        GPIO.output(self.trig,True)
                        time.sleep(0.00001)
                        GPIO.output(self.trig,False)

                        while GPIO.input(self.echo)==False: #peri v2.1
                        #while GPIO.input(echo)==True: #peri v2.0
                              pulse_start=time.time()
                        while GPIO.input(self.echo)==True:
                        #while GPIO.input(echo)==True:
                              pulse_end=time.time()
                        pulse_duration=pulse_end-pulse_start
                        distance=pulse_duration*17000
                        distance=round(distance,2)
                        print("Distance:",distance,"cm")
                        return distance
            except:
                  GPIO.cleanup()

class CLCD(GPIO_BASE):
      # Define GPIO to LCD mapping
      LCD_RS = 23
      LCD_E  = 26
      LCD_D4 = 17
      LCD_D5 = 18
      LCD_D6 = 27
      LCD_D7 = 22
      # Define some device constants
      LCD_WIDTH = 16    # Maximum characters per line
      LCD_CHR = True
      LCD_CMD = False

      LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
      LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line

      # Timing constants
      E_PULSE = 0.0005
      E_DELAY = 0.0005
      def __init__(self):
            GPIO_BASE.__init__(self)
            GPIO.setup(self.LCD_E, GPIO.OUT)  # E
            GPIO.setup(self.LCD_RS, GPIO.OUT) # RS
            GPIO.setup(self.LCD_D4, GPIO.OUT) # DB4
            GPIO.setup(self.LCD_D5, GPIO.OUT) # DB5
            GPIO.setup(self.LCD_D6, GPIO.OUT) # DB6
            GPIO.setup(self.LCD_D7, GPIO.OUT) # DB7
            self.lcd_init()
            self.lcd_byte(0x01, self.LCD_CMD)
            self.lcd_string("Maroro world!!",1)
      def lcd_init(self):
              # Initialise display
              self.lcd_byte(0x33,self.LCD_CMD) # 00110011 Initialise
              self.lcd_byte(0x32,self.LCD_CMD) # 00110010 Initialise
              self.lcd_byte(0x06,self.LCD_CMD) # 00000110 Entry Mode set cursor dir raise no move disp
              self.lcd_byte(0x0C,self.LCD_CMD) # 00001100 Display On,Cursor Off, Blink Off
              self.lcd_byte(0x28,self.LCD_CMD) # 00101000 Data length 4byte, number of lines 2, font size 5x7
              self.lcd_byte(0x01,self.LCD_CMD) # 00000001 Clear display
              time.sleep(self.E_DELAY)

      def lcd_byte(self,bits, mode):
              # Send byte to data pins
              # bits = data
              # mode = True  for character
              #        False for command

              GPIO.output(self.LCD_RS, mode) # RS

              # High bits
              GPIO.output(self.LCD_D4, False)
              GPIO.output(self.LCD_D5, False)
              GPIO.output(self.LCD_D6, False)
              GPIO.output(self.LCD_D7, False)
              if bits&0x10==0x10:
                    GPIO.output(self.LCD_D4, True)
              if bits&0x20==0x20:
                    GPIO.output(self.LCD_D5, True)
              if bits&0x40==0x40:
                    GPIO.output(self.LCD_D6, True)
              if bits&0x80==0x80:
                    GPIO.output(self.LCD_D7, True)

              # Toggle 'Enable' pin
              self.lcd_toggle_enable()

              # Low bits
              GPIO.output(self.LCD_D4, False)
              GPIO.output(self.LCD_D5, False)
              GPIO.output(self.LCD_D6, False)
              GPIO.output(self.LCD_D7, False)
              if bits&0x01==0x01:
                GPIO.output(self.LCD_D4, True)
              if bits&0x02==0x02:
                GPIO.output(self.LCD_D5, True)
              if bits&0x04==0x04:
                GPIO.output(self.LCD_D6, True)
              if bits&0x08==0x08:
                GPIO.output(self.LCD_D7, True)

              # Toggle 'Enable' pin
              self.lcd_toggle_enable()

      def lcd_toggle_enable(self):
              # Toggle enable
              time.sleep(self.E_DELAY)
              GPIO.output(self.LCD_E, True)
              time.sleep(self.E_PULSE)
              GPIO.output(self.LCD_E, False)
              time.sleep(self.E_DELAY)

      def lcd_string(self,message,line):
        # Send string to display
        self.message = message.ljust(self.LCD_WIDTH," ")
        if line==1:
            self.lcd_byte(self.LCD_LINE_1, self.LCD_CMD)
        if line==2:
            self.lcd_byte(self.LCD_LINE_2, self.LCD_CMD)
        for i in range(self.LCD_WIDTH):
              self.lcd_byte(ord(self.message[i]),self.LCD_CHR)# charter to ASCII

class PIR(GPIO_BASE):
    def __init__(self):
          GPIO_BASE.__init__(self)
          print('PIR')
          self.PIR= 24
          GPIO.setup(self.PIR, GPIO.IN)

    def loop(self):
          cnt= 0
          while True:
              if (GPIO.input(self.PIR) == True):
                  cnt+=1
                  print ('detected %d\n' %cnt)

                  #return "detect"
              else:
                  return cnt
              time.sleep(0.1)
    def pir(self):
        try:
            self.loop()
        except KeyboardInterrupt:
            pass
       # finally:
        #    GPIO.cleanup()

#class TEM_HUM(GPIO_BASE):
#    def __init__(Self):
#        GPIO_BASE.__init__(self)
#        print('TEM_HUM')

class MOTOR(GPIO_BASE):
    def __init__(self):
          GPIO_BASE.__init__(self)
          print('MOTOR')

          self.GPIO_RP=4
          self.GPIO_RN=25
          self.GPIO_EN=12

          GPIO.setup(self.GPIO_RP,GPIO.OUT)
          GPIO.setup(self.GPIO_RN,GPIO.OUT)
          GPIO.setup(self.GPIO_EN,GPIO.OUT)

          GPIO.output(self.GPIO_EN,True)

          self.j=JOG()

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
          self.p=GPIO.PWM(12,100)
          self.p.start(0)
          try:
                while True:
                      if self.j.jog_cntl()=='up':
                          print('up')
                          self.duty+=5
                          if self.duty>100:
                              self.duty=100
                          super().Change_DutyCycle(self.p, self.duty)
                          self.motor_forward()
                          time.sleep(0.1)
                      elif self.j.jog_cntl()=='down':
                            print('down')
                            self.duty-=5
                            if self.duty<0:
                                  self.duty=0
                            super().Change_DutyCycle(self.p, self.duty)
                            self.motor_forward()
                            time.sleep(0.1)
                      elif  self.j.jog_cntl()=='left':
                            print('left')
                            if self.duty == 0:
                                  self.p.start(100)
                            self.duty=100
                            super().Change_DutyCycle(self.p, self.duty)
                            self.motor_forward()
                            time.sleep(0.1)

                      elif  self.j.jog_cntl()=='right':
                            print('right')
                            if self.duty== 0:
                                  self.p.start(100)
                                  self.duty=100
                            self.duty=100
                            super().Change_DutyCycle(self.p, self.duty)
                            self.motor_backward()
                            time.sleep(0.1)

                      elif  self.j.jog_cntl()=='center':
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
            self.j=JOG()
            print('led_init')

           # for i in range(5):
                #  GPIO.setup(gpio[i],GPIO.IN)
            for i in self.leds:
                  GPIO.setup(i,GPIO.OUT)
                  GPIO.output( i, False )

      def led_on(self,led_pin):
            self.led_pin=led_pin
            GPIO.output( self.led_pin, True )
      def led_off(self,led_pin):
            self.led_pin=led_pin
            GPIO.output( self.led_pin, False )
      def led_cntl(self):
            self.p1=GPIO.PWM(self.led_pin1,100)
            self.p1.start(0)
            self.p2=GPIO.PWM(self.led_pin2,100)
            self.p2.start(0)
            try:
                  while True:
                        if self.j.jog_cntl()=='up':
                              #led1 off led2 on
                              self.duty+=5
                              if self.duty>100:
                                  self.duty=100
                              super().Change_DutyCycle(self.p1,self.duty)
                              super().Change_DutyCycle(self.p2,self.duty)
                              time.sleep(0.1)
                        elif self.j.jog_cntl()=='down':
                              #led1 on led2 off
                              self.duty-=5
                              if self.duty<0:
                                  self.duty=0
                              super().Change_DutyCycle(self.p1,self.duty)
                              super().Change_DutyCycle(self.p2,self.duty)
                              time.sleep(0.1)
                        elif self.j.jog_cntl()=='left' or self.j.jog_cntl()=='center':
                              #leds on
                              self.led_on(self.led_pin1)
                              self.led_on(self.led_pin2)
                              self.duty=100
                              super().Change_DutyCycle(self.p1,self.duty)
                              super().Change_DutyCycle(self.p2,self.duty)
                        elif self.j.jog_cntl()=='right':
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
      gpio=[5,6,16,20,21]
      def __init__(self):
            #gpio [up, dn, lt, rt, cen]
            gpio=[5,6,16,20,21]
            super().__init__()
            for i in range(5):
                  GPIO.setup(gpio[i],GPIO.IN)
      def jog_cntl(self):
                  while True:
                        if GPIO.input(self.gpio[0]):
                              return 'up'
                        elif GPIO.input(self.gpio[1]):
                              return 'down'
                        elif GPIO.input(self.gpio[2]):
                              return 'left'
                        elif GPIO.input(self.gpio[3]):
                              return 'right'
                        elif GPIO.input(self.gpio[4]):
                              return 'center'


if __name__=='__main__':

      base=GPIO_BASE()
      ld=LED()
      mt=MOTOR()
      #mt.motor_cntl()
      ld.led_cntl()
      cl=CLCD()
      cl.lcd_string("himaro",2)
      #pie=PIEZO()
      #pie.piezo()
      us=UltSon()
      #us.ultson()
      #p=PIR()
      #p.pir()
