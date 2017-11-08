import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led_pin1=14
led_pin2=15



def led_init(leds):
    print('led_init')
    for i in leds:
        GPIO.setup(i,GPIO.OUT)

    
def led_on(leds):
    print('led_on')
    for i in leds:
        GPIO.output(i,True)
    
def led_off(leds):
    for i in leds:
        GPIO.output(i,False)
       
def led_blink(leds,delay):
        print('led_blink on')
        for i in leds:
            GPIO.output(i,True)
        time.sleep(delay)
        print('led_blink off')
        for i in leds:
            GPIO.output(i,False)
        time.sleep(delay)
        print('led_blink finish')
def led_shift(leds,delay):
    print('led_shift')
    for i in leds:
        GPIO.output(i,True)
        time.sleep(delay)
        GPIO.output(i,False)
        time.sleep(delay)
    print('led_shift finish')



    
if __name__=='__main__':
    leds=(led_pin1,led_pin2)
    led_init(leds)
    led_off(leds)
    time.sleep(1)
    led_on(leds)
    time.sleep(1)
    print('led_off')
    led_off(leds)
    delay=int(input('enter delay:'))
    led_blink(leds,delay)
    time.sleep(1)
    delay=int(input('enter shift delay:'))
    led_shift(leds,delay)
    time.sleep(1)
    led_off(leds)
    print("Cleaning up")
    GPIO.cleanup()
    