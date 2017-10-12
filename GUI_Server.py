from tkinter import *
from tkinter import ttk
from tkinter import messagebox
#import team1_GPIO as r
#import team1_I2C as i2c
import time
import pccon
class DISPLAY():
	def __init__(self):
		self.root = Tk()
		self.root.title("sensor ckeck in server")

		self.root.geometry("970x1000+10+10")
		self.root.resizable(0,0)

		self.label1=Label(text='센서 제어판', font=('나눔스퀘어 ExtraBold', 14))
		self.label1.pack(anchor=N, ipadx = 800, ipady = 20)

		self.frameleft= Frame(self.root)
		self.frameright = Frame(self.root)
		self.frameleft.pack(side =LEFT, padx = 4, fill=BOTH)
		self.frameright.pack(side = LEFT, fill=BOTH)

		self.frame1 = Frame(self.frameleft, background ="yellow" )
		self.frame2 = Frame(self.frameleft, background ="purple" )
		self.frame3 = Frame(self.frameleft, background ="yellow" )
		self.frame4 = Frame(self.frameleft, background ="purple")
		self.frame5 = Frame(self.frameleft, background ="yellow")
		self.frame6 = Frame(self.frameright, background ="purple" )
		self.frame7 = Frame(self.frameright, background ="yellow" )
		self.frame8 = Frame(self.frameright, background ="purple" )
		self.frame9 = Frame(self.frameright, background ="yellow" )
		self.frame10 = Frame(self.frameright, background ="purple" )

		self.frame1.pack(fill=BOTH)
		self.frame2.pack(ipadx = 30, ipady = 40, fill=BOTH)
		self.frame3.pack(ipadx = 20, ipady = 30, fill=BOTH)
		self.frame4.pack(ipadx = 5, ipady = 5, fill=BOTH)
		self.frame5.pack(ipadx = 30, ipady = 40, fill=BOTH)
		self.frame6.pack(ipadx = 20, ipady = 30, fill=BOTH)
		self.frame7.pack(ipadx = 40, ipady = 50, fill=BOTH)
		self.frame8.pack(ipadx = 50, ipady = 60, fill=BOTH)
		self.frame9.pack(ipadx = 10, ipady = 20, fill=BOTH)
		self.frame10.pack(ipadx = 30, ipady = 40, fill=BOTH)

		title_led = Label(self.frame1, text="1 LED", width = 15, \
		                                  font=('나눔스퀘어 ExtraBold', 14))
		title_motor = Label(self.frame2, text="2 DCMotor", width = 15, \
                                  font=('나눔스퀘어 ExtraBold', 14))
		title_jog = Label(self.frame3, text="3 JogSwitch" , width = 15, \
                                  font=('나눔스퀘어 ExtraBold', 14))
		title_clcd = Label(self.frame4, text="4 CLCD", width = 15, \
                                  font=('나눔스퀘어 ExtraBold', 14))
		title_ultra = Label(self.frame5, text="5 Ultrasonic" , width = 15, \
                                  font=('나눔스퀘어 ExtraBold', 14))
		title_piezo = Label(self.frame6, text="6 Piezo", width = 15, \
                                  font=('나눔스퀘어 ExtraBold', 14))
		title_pir = Label(self.frame7, text="7 PIR", width = 15, \
                                  font=('나눔스퀘어 ExtraBold', 14))
		title_light = Label(self.frame8, text="8 LightSensor", width = 15, \
                                  font=('나눔스퀘어 ExtraBold', 14))
		title_tmhm = Label(self.frame9, text="9 TempHumid", width = 15, \
                                  font=('나눔스퀘어 ExtraBold', 14))
		title_fnd = Label(self.frame10, text="10 FND", width = 15, \
                                  font=('나눔스퀘어 ExtraBold', 14))
		self.led_state = Label(self.frame1, text = "LED상태", font =20)

		title_led.grid(row=0, column=0)
		title_motor.grid(row=0, column=0)
		title_jog.grid(row=0, column=0)
		title_clcd.grid(row=0, column=0)
		title_ultra.grid(row=0, column=0)
		title_piezo.grid(row=0, column=0)
		title_pir.grid(row=0, column=0)
		title_light.grid(row=0, column=0)
		title_tmhm.grid(row=0, column=0)
		title_fnd.grid(row=0, column=0)

		self.Lflag1 = 0
		self.Lflag2 = 0
		self.Mflag = 0
		self.Pflag = 0

                #3jog
		jog_monitor = Label(self.frame3, text="JogSwitch",width = 30, height = 3)
		jog_monitor.grid(row=1, column=3, padx=5, pady=5, columnspan=2)

                #4 clcd

		clcd_textbox =  Entry(self.frame4, text="값 입력창 ")
		clcd_textbox.grid(column=2, row=1, padx=5, pady=5)

		btn_clcd_ok = Button(self.frame4, text = "OK", width = 8, height = 2)
		btn_clcd_ok.grid(row=3, column=2, padx=5, pady=5)

		clcd_label = Label(self.frame4, text='문자를 입력하세요', height = 3)
		clcd_label.grid(column=1, row=1,padx=5, pady=5)
                #5 ultrasonic
		ultra_action = Button(self.frame5, text="거리값 알아보기")
		ultra_action.grid(column=2, row=1, padx=5, pady=5, columnspan=2)

		#6 piezo
		btn_piezo_power = Button(self.frame6, width = 12, height = 2, text = "On")
		btn_piezo_power.grid(row=1, column=3, padx=5, pady=5, columnspan=2 )

		#7 PIR
		pir_label = Label(self.frame7, text='PIR: 감지여부', font = 20)
		pir_label.grid(column=2, row=1, padx=5, pady=5,)

		#8 lightsensor
		pir_label = Label(self.frame8, text='Light Sensor : 밝기값', font = 20)
		pir_label.grid(column=2, row=1, padx=5, pady=5)

		#9 FND
		fnd_label = Label(self.frame9, text='숫자를 입력하세요')
		fnd_label.grid(column=1, row=1, padx=5, pady=5)

		fnd_textbox =  Entry(self.frame9, text="값 입력창 ")
		fnd_textbox.grid(column=2, row=1, padx=5, pady=5)

		fnd_action = Button(self.frame9, text="OK", width = 8, height = 2)
		fnd_action.grid(column=2, row=2, padx=5, pady=5)

		#10 Temp/Humid
		pir_label = Label(self.frame10, text='Temp/Humid : 온/습도값', font = 20)
		pir_label.grid(column=2, row=1, padx=5, pady=5)
		self.pc=pccon.Pcon()
	def led1(self):
		if self.Lflag1 == 1:
			self.btn_led1_power.config(text= "LED1 Off")
			self.Lflag1 =0
		elif self.Lflag1 == 0:
			self.btn_led1_power.config(text= "LED1 On")
			self.Lflag1 = 1
		
		self.pc.pcsend('00')

	def led2(self):
		if self.Lflag2 == 1:
			self.btn_led2_power.config(text= "LED2 Off")

			self.Lflag2 =0

		elif self.Lflag2 == 0:
			self.btn_led2_power.config(text= "LED2 On")
			self.Lflag2 = 1
		self.pc.pcsend('01')

	def dcm(self):
		if self.Mflag == 0:
			self.btn_motor_power.config(text = "Off")
			self.Mflag =1
		elif self.Mflag == 1:
			self.btn_motor_power.config(text = "On")
			self.Mflag =0
		
		self.pc.pcsend('20')


	def event(self):
        ##1 LED
		self.btn_led1_power = Button(self.frame1, width = 10, height = 2, text = "LED1 On", command = self.led1)
		self.btn_led2_power = Button(self.frame1, width = 10, height = 2, text = "LED2 On", command = self.led2)
		#체크박스 만들어야 할듯
		self.btn_led1_up = Button(self.frame1, width = 10, height = 2, text = "LED1 Light ▲")
		self.btn_led1_dn = Button(self.frame1, width = 10, height = 2, text = "LED1 Light ▼")
		self.btn_led2_up = Button(self.frame1, width = 10, height = 2, text ="LED2 Light ▲")
		self.btn_led2_dn = Button(self.frame1, width = 10, height = 2, text ="LED2 Light ▼")


		self.led_state.grid(row = 1, column=2)
		self.btn_led1_power.grid(row=2, column=2, padx=5, pady=5)
		self.btn_led2_power.grid(row=2, column=3, padx=5, pady=5)
		self.btn_led1_up.grid(row=3, column=2,padx=5, pady=5)
		self.btn_led1_dn.grid(row=3, column=3,padx=5, pady=5)
		self.btn_led2_up.grid(row=4, column=2,padx=5, pady=5)
		self.btn_led2_dn.grid(row=4, column=3,padx=5, pady=5)

		##2 모터
		btn_state = Label(self.frame2, text = "Btn  상태 ", font = 20)
		self.btn_motor_power = Button(self.frame2, width = 20, text = "On", command = self.dcm)
		self.btn_motor_up = Button(self.frame2, width = 10, text = "UP")
		self.btn_motor_dn = Button(self.frame2, width = 10, text = "DN")
		self.btn_motor_dir = Button(self.frame2, width = 20, text = "Spin 방향변경")

		btn_state.grid(row=1, column=0, padx=5, pady=5 )
		self.btn_motor_power.grid(row=2, column=1, padx=5, pady=5)
		self.btn_motor_up.grid(row=3, column=1, padx=5, pady=5)
		self.btn_motor_dn.grid(row=3, column=2, padx=5, pady=5)
		self.btn_motor_dir.grid(row=4, column=1, padx=5, pady=5)

		##3 조그스위치

		self.root.mainloop()


if __name__=='__main__':
      w = DISPLAY()
      w.event()
