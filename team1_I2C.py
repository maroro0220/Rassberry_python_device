import smbus2 as smbus
import time

class I2C_Base:
    DELAY = 0.26

    def __init__( self, addr ):
        self.addr = addr
        self.bus = smbus.SMBus( 1 )
        self.data = [ 0, 0 ]
        self.val = 0

    def explain( self ):
        print('''
------------------------------
LightSensor / TempHumid / FND
------------------------------
        ''')

    def readData( self ):
        for i in range(2):
            self.data[i] = self.bus.read_byte( self.addr )
        self.val = ( self.data[0] << 8 ) | self.data[1]
        return self.val

    def writeData( self, contents ):
        self.bus.write_byte( self.addr, contents )
        time.sleep( self.DELAY )


class LightSensor( I2C_Base ):
    LIGHT_ADDR = 0X23
    LIGHT_RESET = 0X07
    LIGHT_HR_MODE =0X10

    def __init__( self ):
        super().__init__( self.LIGHT_ADDR )
        self.light_val = 0
        self.brightness = ''
        self.bus.write_byte( self.addr, self.LIGHT_RESET )
        time.sleep( self.DELAY )

    def explain( self ):
        print('''
< LightSensor >
    check_light()     - check light and return illumination
                      ''')

    def check_light( self ):
        try:
            self.writeData( self.LIGHT_HR_MODE )
            time.sleep( self.DELAY )

            self.light_val = self.readData() / 1.2
            self.light_val = round( self.light_val, 2 )

            if self.light_val < 200.0:
                self.brightness = 'dark'
            elif 200.0 <= self.light_val < 1000.0:
                self.brightness = 'normal'
            elif self.light_val >= 1000.0:
                self.brightness = 'bright'
            return self.brightness
        except KeyboardInterrupt:
            pass
        finally:
            pass

class TempHumid( I2C_Base ):
    TEMP_HUMID_ADDR = 0X40
    CMD_TEMP = 0XF3
    CMD_HUMI = 0XF5
    SOFT_RESET = 0XFE

    def __init__( self ):
        super().__init__( self.TEMP_HUMID_ADDR )
        self.temp = 0.0
        self.humi = 0.0
        self.bus.write_byte( self.addr, self.SOFT_RESET )
        time.sleep( self.DELAY )

    def explain( self ):
        print('''
< TempHumid >
    check_temp()     - check temperature and return temperature
    check_humid()    - check humidity and return humidity
                      ''')

    def check_temp( self ):
        try:
            self.writeData( self.CMD_TEMP )
            time.sleep( self.DELAY )

            self.temp = -46.85 + 175.22 / 65536 * self.readData()
            return round( self.temp, 2)
        except KeyboardInterrupt:
            pass
        finally:
            pass

    def check_humid( self ):
        try:
            self.writeData( self.CMD_HUMI )
            time.sleep( self.DELAY )

            self.humi = -6.0 + 125.0 / 65536 * self.readData()
            return round( self.humi, 2)
        except KeyboardInterrupt:
            pass
        finally:
            pass

class FND( I2C_Base ):
    FND_ADDR = 0X20
    CONFIG_PORT = 0X06
    OUT_PORT = 0X02
    FND_CLEAN = 0X0003
    #        0      1     2     3     4     5     6     7    8     9
    NUM = ( 0XFC, 0X60, 0XDA, 0XF2, 0X66, 0XB6, 0X3E, 0XE0, 0XFE, 0XF6 )
    #         seg6, seg5, seg4, seg3, seg2, seg1
    DIGIT = ( 0XFB, 0XF7, 0XEF, 0XDF, 0XBF, 0X7F )
    #         seg1, seg2, seg3, seg4, seg5, seg6
    DIGIT2 = ( 0X7F, 0XBF, 0XDF, 0XEF, 0XF7, 0XFB )

    def __init__( self ):
        super().__init__( self.FND_ADDR )
        self.bus.write_word_data( self.addr, self.CONFIG_PORT, 0X0000)
        self.temp = []

    def explain( self ):
        print('''
< FND >
    printFND( place, number )     - print number at specific place
    FNDprint( number )    - print number
                      ''')

    def printFND( self, where, num ):
        self.val = ( self.NUM[num] << 8 ) | self.DIGIT2[where-1]
        try:
            self.bus.write_word_data( self.addr, self.OUT_PORT, self.val )
            time.sleep(0.1)
        except KeyboardInterrupt:
            pass

    def FNDprint( self, number ):
        self.bus.write_word_data( self.addr, self.OUT_PORT, self.FND_CLEAN )
        self.temp = []
        number = str( number )
        number = ''.join( reversed( number ) )

        for i in range( len( number ) ):
            self.temp.append( number[ i : i + 1 ] )

        while True :
            for i in range( len( self.temp ) ):
                for j in range( len( self.NUM ) ):
                    if self.temp[i] == str( j ) :
                        self.val = ( self.NUM[ j ] << 8 ) | self.DIGIT[ i ]
                        self.bus.write_word_data( self.addr, self.OUT_PORT, self.val )
                        time.sleep( 0.005 )
