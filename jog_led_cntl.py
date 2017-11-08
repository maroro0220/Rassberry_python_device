import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
#gpio [up, dn, lt, rt, cen]
gpio=[ 5,  6,  16, 20, 21]
#stat [up, dn, lt, rt, cen]
stat =[0,  0,  0,  0,  0]

led_pin1=14
led_pin2=15

GPIO.setwarnings(False)
def led_init(leds):
    print('led_init')
    for i in leds:
        GPIO.setup(i,GPIO.OUT)
def led_on( led_pin ):
        GPIO.output( led_pin, True )

def led_off( led_pin ):
        GPIO.output( led_pin, False )
def jog():
      
      try:
            for i in range(5):
                  GPIO.setup(gpio[i],GPIO.IN)
      
            while True:
                  if GPIO.input(gpio[0]):
                        #led1 off led2 on
                        led_on(led_pin1)
                        led_off(led_pin2)
                  elif GPIO.input(gpio[1]):
                        #led1 on led2 off
                        led_on(led_pin2)
                        led_off(led_pin1)
                  elif GPIO.input(gpio[2]) or GPIO.input(gpio[4]):
                        #leds on
                        led_on(led_pin1)
                        led_on(led_pin2)
                  elif GPIO.input(gpio[3]):
                        #leds off
                        led_off(led_pin1)
                        led_off(led_pin2)

    
      finally:
            print("Cleaning up")
            GPIO.cleanup()

            
if __init__=='__main__':
      
      leds=(led_pin1,led_pin2)
      led_init(leds)
