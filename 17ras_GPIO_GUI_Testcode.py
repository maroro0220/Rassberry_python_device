from tkinter import *
import YESGPIO as yes
import RPi.GPIO as GPIO
import time

def windowEx():
    led1 = 0
    led2 = 0
    motor = 0
    window = Tk()

    window.title( 'GPIO control' )
    window.geometry( '400x200' )
    window.resizable( width = TRUE, height = TRUE )

    LED = yes.LED()
    MOTOR = yes.DCMotor()

    def led1_btn_event():
        nonlocal led1
        if led1 == 0 :
            led1_btn.config( text = 'led1_off' )
            LED.led1_on()
            time.sleep(0.1)
            led1 = 1
        elif led1 == 1:
            led1_btn.config( text = 'led1_on')
            LED.led1_off()
            time.sleep(0.1)
            led1 = 0

    def led2_btn_event():
        nonlocal led2
        if led2 == 0:
            led2_btn.config( text = 'led2_off' )
            LED.led2_on()
            led2 = 1
        elif led2 == 1:
            led2_btn.config( text = 'led2_on')
            LED.led2_off()
            led2 = 0

    def led1_up_event():
        LED.led1_adjust('up')

    def led1_dn_event():
        LED.led1_adjust('down')

    def led2_up_event():
        LED.led2_adjust('up')

    def led2_dn_event():
        LED.led2_adjust('down')


    def motor_btn_event():
        nonlocal motor
        if motor == 0:
            motor_btn.config( text = 'motor_off' )
            MOTOR.cw()
            motor = 1
        elif motor == 1:
            motor_btn.config( text = 'motor_on')
            MOTOR.stop()
            motor = 0

    def piezo_btn_event():
        PIEZO.lalal()

    led1_btn = Button( window, text = 'led1_on', width = 10, height = 3,\
                        font = ('나눔스퀘어 ExtraBold', 10), command = led1_btn_event )

    led2_btn = Button( window, text = 'led2_on', width = 10, height = 3,\
                        font = ('나눔스퀘어 ExtraBold', 10), command = led2_btn_event )

    led1_up_btn = Button( window, text = 'led1_up', width = 10, height = 3,\
                        font = ('나눔스퀘어 ExtraBold', 10), command = led1_up_event )

    led1_dn_btn = Button( window, text = 'led1_dn', width = 10, height = 3,\
                        font = ('나눔스퀘어 ExtraBold', 10), command = led1_dn_event )

    led2_up_btn = Button( window, text = 'led2_up', width = 10, height = 3,\
                        font = ('나눔스퀘어 ExtraBold', 10), command = led2_up_event )

    led2_dn_btn = Button( window, text = 'led2_dn', width = 10, height = 3,\
                        font = ('나눔스퀘어 ExtraBold', 10), command = led2_dn_event )

    motor_btn = Button( window, text = 'motor_on', width = 10, height = 3,\
                        font = ('나눔스퀘어 ExtraBold', 10), command = motor_btn_event )


    led1_btn.pack()
    led2_btn.pack()
    led1_up_btn.pack()
    led1_dn_btn.pack()
    led2_up_btn.pack()
    led2_dn_btn.pack()
    motor_btn.pack()
    window.mainloop()


if __name__ == '__main__':
    windowEx()
