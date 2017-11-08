import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

trig=0
echo=1

GPIO.setup(trig,GPIO.OUT)
GPIO.setup(echo,GPIO.IN)  #Peri v2.1
#GPIO.setup(echo, GPIO.IN, GPIO.PUD_UP) #peri v2.0

try:
      while True:
            GPIO.output(trig,False)
            time.sleep(0.5)

            GPIO.output(trig,True)
            time.sleep(0.00001)
            GPIO.output(trig,False)

            while GPIO.input(echo)==False: #peri v2.1
            #while GPIO.input(echo)==True: #peri v2.0
                  pulse_start=time.time()
            while GPIO.input(echo)==True:
            #while GPIO.input(echo)==True:
                  pulse_end=time.time()
            pulse_duration=pulse_end-pulse_start
            distance=pulse_duration*17000
            distance=round(distance,2)

            print("Distance:",distance,"cm")
except:
      GPIO.cleanup()
