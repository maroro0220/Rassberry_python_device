import sqlite3

# data format
# LED data = ( LED, time, state1, state2 )  LED/cnt,time,state1,state2
# DCMotor = ( DCMotor, time, state, direction, speed )
# JogSwitch = ( JogSwitch, time, direction )
# CharacterLCD = ( CharacterLCD, time, line1_text, line2_text )
# Ultrasonic = ( Ultrasonic, time, distance )
# Piezo = ( Piezo, time, state )
# PIR = ( PIR, time, state )
# LightSensor = ( LightSensor, time, light_value )
# TempHumid = ( TempHumid, time, temp, humid )
# FND = ( FND, time, number )


class tema1_DB:

    def __init__(self):
        self.conn = sqlite3.connect('team1_DB.db')
        self.curs = self.conn.cursor()
        self.table = ''
        self.value = ''


    def insert_data(self, data):
        #print(type(data))
        self.table = data[0]
        #print(type(data[1]))
#        for x in range( len(data) - 1 ):
#            self.value += data[ x + 1 ]
#            if x < ( len(data) - 2 ):
#                self.value += ', '
        field=tuple(data[1].split(','))
        print(field)
        print(len(field))
        sql = 'insert into '+ self.table+' values (?, ?, ?, ?, ?, ?)'
        self.curs.execute(sql, field)
        self.conn.commit()
        #self.conn.close()

