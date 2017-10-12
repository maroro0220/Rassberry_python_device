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
        self.label1_2 = Label(self.frame1, text = "LED1 : on/off, 밝기 \n")
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
        self.label2_2.pack()
        self.label3_2.pack()
        self.label4_2.pack()
        self.label5_2.pack()
        self.label6_2.pack()
        self.label7_2.pack()
        self.label8_2.pack()
        self.label9_2.pack()
        self.label10_2.pack()

        self.win.mainloop()

    def led_1_config(self,state,lux):
        self.label1_2.config( text="LED1:"+state+str(lux)+"\n")
    def led_2_config(self,on,lux):
        self.label1_2_1.config(self.frame1, text="LED2:"+on+str(lux)+"\n")
    def Motor_config(self,on,direction,speed):
        self.label1_2.config(self.frame2, text="Motor : "+on+ "방향 : " + direction +"\n"+ "speed : " + speed)
    def Jog_config(self,direction):
        self.label3_2.config = Label(self.frame3, text = "방향 : " + direction+"\n" )
    def CLCD_config(self,texts):
        self.label4_2.config = Label(self.frame4, text = "입력한 텍스트 : " + texts+"\n")
    def Ultra_config(self,distance):
        self.label5_2.config = Label(self.frame5, text = "거리값 : " + distance + "\n")
    def Piezo_config(self,on):
        self.label6_2.config = Label(self.frame6, text = "on/off : " + on +"\n")
    def PIR(self, sensing):
        self.label7_2.config = Label(self.frame7, text = "감지여부 : " + sensing + "\n")
    def Light(self,lux):
        self.label8_2.config = Label(self.frame8, text = "밝기 값 : " + lux + "\n")
    def FND(self,number):
        self.label9_2.config = Label(self.frame9, text = "입력한 숫자 : " + number+"\n")
    def Temp_Humid(self,temp,humid):
        self.label10_2.config = Label(self.frame10, text = "온도값 : " + temp+ "습도값 : " + humid+"\n")


if __name__=='__main__':
    w=WindowClient()
    w.Values()
    w.led_1_config('off',123)
