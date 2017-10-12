import team1_GPIO as gp
import team1_I2C as i2c
from time import localtime, strftime

class DV_Module:
    def __init__(self):
        self.led=gp.LED()           #0,1
        self.dm=gp.DCMotor()        #2
        self.pie=gp.Piezo()         #3
        self.fnd=i2c.FND()          #4
        self.clcd=gp.CharacterLCD() #5
        self.jog=gp.JogSwitch()     #6
        self.uso=gp.Ultrasonic()    #7
        self.pir=gp.PIR()           #8
        self.lse=i2c.LightSensor()  #9
        self.thu=i2c.TempHumid()    #10

        #status flag
        self.led1stat = False
        self.led2stat = False
        self.dmstat = False
        self.dmcw = False           #motor direction
        #False = cw, True = ccw

        self.output = 0;
        self.count = [0]*9

""""
data numbering
00 = led1 on/off
01 = led1 pwm up
02 = led1 pwm down
10 = led2 on/off
11 = led2 pwm up
12 = led2 pwm down
20 = DCmotor on(cw)/off
21 = DCmotor cw/cww
22 = DCmotor speed up
23 = DCmotor speed down
30 = Piezo on/off
4xxxx = FND
5xxxx = CLCD
"""
    def con_module(self,data):
        if data=='00':
            if led1stat == False:
                self.led.led1_on()
            else:
                self.led.led1_off()
            !self.led1stat
            self.output = 0
        elif data =='01':
            self.led.led1_adjust('up')
            self.output = 0
        elif data =='02':
            self.led.led1_adjust('down')
            self.output = 0
        elif data=='10':
            if led2stat == False:
                self.led.led2_on()
            else:
                self.led.led2_off()
            !self.led2stat
            self.output = 1
        elif data =='11':
            self.led.led2_adjust('up')
            self.output = 1
        elif data =='12':
            self.led.led2_adjust('down')
            self.output = 1
        elif data=='20':
            if dmstat = False:
                self.dm.cw()
                self.dmcw = False
            else:
                self.dm.stop()
            !self.dmstat
            self.output = 2
        elif data=='21':
            if dmcw==False:
                self.dm.ccw()
                !self.dmcw
            else:
                self.dm.cw()
                !self.dmcw()
            self.output = 2
        elif data=='22':
            self.dm.speed_up()
            self.output = 2
        elif data=='23':
            self.dm.speed_down()
            self.output = 2
        elif data=='30':
            self.pie.lalala()
            self.output = 3
        elif data[0]=='4':
            self.fnd.FNDprint(data[1:])
            self.output = 4
        elif data[0]=='5':
            self.lcd_string(data[1:], 0)
            self.output = 5
        return self.output

    def set_str(self):
        if self.output == 0 || self.output == 1:    #LCD1,2  count[0]
            outputdata = 'LED/' + str(self.count[0]) + \
            ', ' + strftime("%Y-%m-%d %I:%M:%S",localtime()) + ', '
            if self.led1stat == True:
                outputdata += 'on, '
            else:
                outputdata += 'off, '

            if self.led2stat == True:
                outputdata += 'on, '
            else:
                outputdata += 'off, '

            outputdata = outputdata + str(self.led.brightness1) + ', ' \
            + str(self.led.brightness2)

            self.count[0] += 1

        elif self.output == 2:  #DCMotor  count[1]
            outputdata = 'DCMotor/' + str(self.count[1]) + \
            ', ' + strftime("%Y-%m-%d %I:%M:%S",localtime()) + ', '

            if self.dmstat == True:
                outputdata += 'on, '
            else:
                outputdata += 'off, '

            if self.dmcw == True:
                outputdata += 'ccw, '
            else:
                outputdata += 'cw, '

            outputdata += str(self.dm.speed)
            self.count[1] += 1

        return outputdata
