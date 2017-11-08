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
    
def pwm_init(leds,i):
    print('led_pwm_init')
    p=GPIO.PWM(leds[i-1],100)
    return p
def pwm(leds,p):
    p.start(0)
    while True:
        for i in range(0,101,5):
            p.ChangeDutyCycle(i)
            time.sleep(0.1)
        for i in range(100,-1,-5):
            p.ChangeDutyCycle(i)
            time.sleep(0.1)
  #      p.stop()
  #      break


    
if __name__=='__main__':
    leds=(led_pin1,led_pin2)
    led_init(leds)
    p=pwm_init(leds,1)
    pwm(leds,p)
    print("Cleaning up")
    GPIO.cleanup()
    