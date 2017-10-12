from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#import team1_GPIO as r
#import team1_I2C as i2c
import time

class WindowClient():
    def __init__(self):
        self.win = Tk()
        self.win.title("현재 Sensor 상태 Display")
        self.win.geometry("950x600")

        self.frameleft = Frame(self.win)
        self.frameright = Frame(self.win)


        self.frame1 = Frame(self.frameleft)
        self.frame2 = Frame(self.frameleft)
        self.frame3 = Frame(self.frameleft)
        self.frame4 = Frame(self.frameleft)
        self.frame5 = Frame(self.frameleft)
        self.frame6 = Frame(self.frameright)
        self.frame7 = Frame(self.frameright)
        self.frame8 = Frame(self.frameright)
        self.frame9 = Frame(self.frameright)
        self.frame10 = Frame(self.frameright)

        self.frameleft.pack(side = LEFT)
        self.frameright.pack(side = RIGHT)

        self.frame1.pack(ipadx = 200, ipady = 30)
        self.frame2.pack(ipadx = 200, ipady = 30)
        self.frame3.pack(ipadx = 200, ipady = 30)
        self.frame4.pack(ipadx = 200, ipady = 30)
        self.frame5.pack(ipadx = 200, ipady = 30)
        self.frame6.pack(ipadx = 200, ipady = 30)
        self.frame7.pack(ipadx = 200, ipady = 30)
        self.frame8.pack(ipadx = 200, ipady = 30)
        self.frame9.pack(ipadx = 200, ipady = 30)
        self.frame10.pack(ipadx = 200, ipady = 30)

        self.label1_1 = Label(self.frame1, text = "LED",font=14)
        self.label2_1 = Label(self.frame2, text = "DC_MOTOR",font=14)
        self.label3_1 = Label(self.frame3, text = "JogSwitch",font=14)
        self.label4_1 = Label(self.frame4, text = "CLCD",font=14)
        self.label5_1 = Label(self.frame5, text = "UltraSonic",font=14)
        self.label6_1 = Label(self.frame6, text = "Piezo",font=14)
        self.label7_1 = Label(self.frame7, text = "PIR",font=14)
        self.label8_1 = Label(self.frame8, text = "Light Sensor",font=14)
        self.label9_1 = Label(self.frame9, text = "FND",font=14)
        self.label10_1 = Label(self.frame10, text = "Temp/Humid",font=14)

        self.label1_1.pack()
        self.label2_1.pack()
        self.label3_1.pack()
        self.label4_1.pack()
        self.label5_1.pack()
        self.label6_1.pack()
        self.label7_1.pack()
        self.label8_1.pack()
        self.label9_1.pack()
        self.label10_1.pack()

    def Values(self):
        
        self.label1_2 = Label(self.frame1, text = "LED1 : on/off, 밝기" )
        self.label1_2_1 = Label(self.frame1, text = "LED2 : on/off, 밝기 \n")
        self.label2_2 = Label(self.frame2, text = "on/off, 방향, \n" + "스피드(0~100) : ")
        self.label3_2 = Label(self.frame3, text = "방향 : \n" + " ")
        self.label4_2 = Label(self.frame4, text = "입력한 텍스트 : \n" + " ")
        self.label5_2 = Label(self.frame5, text = "거리값 : \n" + " ")
        self.label6_2 = Label(self.frame6, text = "on/off : \n" + " ")
        self.label7_2 = Label(self.frame7, text = "감지여부 : \n" + " ")
        self.label8_2 = Label(self.frame8, text = "밝기 값 : \n" + " ")
        self.label9_2 = Label(self.frame9, text = "입력한 숫자 :  \n" + " ")
        self.label10_2 = Label(self.frame10, text = "온도값 : \n" + "습도값 : ")


        self.label1_2.pack()
        self.label1_2_1.pack()
        self.label2_2.pack()
        self.label3_2.pack()
        self.label4_2.pack()
        self.label5_2.pack()
        self.label6_2.pack()
        self.label7_2.pack()
        self.label8_2.pack()
        self.label9_2.pack()
        self.label10_2.pack()

        #self.win.loop()

    def led_1_config(self,state,lux):
        self.label1_2.config(text="LED1 : "+state+" , "+str(lux))
        self.win.update()
    def led_2_config(self,state,lux):
        self.label1_2_1.config(text="LED2 : "+state+" , "+str(lux))
        self.win.update()
    def Motor_config(self,state,direction,speed):
        self.label2_2.config(text="Motor : "+state + "\n"+ "방향 : " + direction + "\n"+ "speed : " + str(speed))
        self.win.update()
    def Jog_config(self,direction):
        self.label3_2.config(text= "방향 : " + direction) 
        self.win.update()
    def CLCD_config(self,texts):
        self.label4_2.config(text = "입력한 텍스트 : " + texts)
        self.win.update()
    def Ultra_config(self,distance):
        self.label5_2.config(text = "거리값 : " + str(distance) + "cm" + "\n")
        self.win.update()
    def Piezo_config(self,state):
        self.label6_2.config(text = "on/off : " + state +"\n")
        self.win.update()
    def PIR(self, sensing):
        self.label7_2.config(text = "감지여부 : " + sensing + "\n")
        self.win.update()
    def Light(self,lux):
        self.label8_2.config(text = "밝기 값 : " + str(lux) + " lux"+"\n")
        self.win.update()
    def FND(self,number):
        self.label9_2.config(text = "입력한 숫자 : " + str(number) +"\n")
        self.win.update()
    def Temp_Humid(self,temp,humid):
        self.label10_2.config(text = "온도값 : " + str(temp) + " C" + "\n" + "습도값 : " + str(humid)+"\n")
        self.win.update()


if __name__=='__main__':
    w=WindowClient()
    w.Values()
    w.led_1_config('off',123)
    w.led_2_config('off',12345)
    w.Motor_config('off','p',50)
    w.Jog_config('up')
    w.CLCD_config('abcdefg')
    w.Ultra_config(3.14)
    w.Piezo_config('on')
    w.PIR("감지")
    w.Light(222)
    w.FND(1234456)
    w.Temp_Humid(23,44)
