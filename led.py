import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
led_pin1=14
led_pin2=15



def led_init(leds):
    GPIO.setup(leds[0],GPIO.OUT)
    GPIO.setup(leds[1],GPIO.OUT)

    
def led_on(leds):
    print('led on')
    GPIO.output(leds[0],True)
    GPIO.output(leds[1],True)
    
def led_off(leds):
    GPIO.output(leds[0],False)
    GPIO.output(leds[1],False)

def led_blink(leds,delay):
        GPIO.output(leds[0],True)
        GPIO.output(leds[1],True)
        time.sleep(delay)
        GPIO.output(leds[0],False)
        GPIO.output(leds[1],False)
        time.sleep(delay)

def led_shift(leds,delay):
    GPIO.output(leds[0],True)
    GPIO.output(leds[1],False)
    time.sleep(delay)
    GPIO.output(leds[0],False)
    GPIO.output(leds[1],True)
    time.sleep(delay)



    
if __name__=='__main__':
    leds=(led_pin1,led_pin2)
    led_init(leds)
    led_off(leds)
    time.sleep(1)
    led_on(leds)
    time.sleep(1)
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
    