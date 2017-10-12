import RPi.GPIO as GPIO
import time

class GPIO_Base:
    def __init__( self, pin ):
        GPIO.setmode( GPIO.BCM )
        GPIO.setwarnings( False )
        self.pin = pin
        self.pwm_start = 0

    def explain( self ):
        print('''
--------------------------------------------------------------------
LED / DCMotor / JogSwitch / CharacterLCD / Ultrasonic / Piezo / PIR
--------------------------------------------------------------------
        ''')

    def set_output( self, pin ):
        GPIO.setup( pin, GPIO.OUT )

    def set_input( self, pin ):
        GPIO.setup( pin, GPIO.IN )

    def set_PWM( self, pin, pwm_start):
        self.pwm_start = pwm_start
        self.PWM = GPIO.PWM( pin, self.pwm_start )
        return self.PWM

class LED( GPIO_Base ):
    LEDS = [ 14, 15 ]

    def __init__( self ):
        super().__init__( self.LEDS )
        super().set_output( self.LEDS )
        GPIO.output( self.pin, False )
        self.AD1 = super().set_PWM( self.LEDS[0], 100 )
        self.AD2 = super().set_PWM( self.LEDS[1], 100 )
        self.brightness1 = 100
        self.brightness2 = 100

    def explain( self ):
        print('''
< LED >
    led1_on()       - LED1 on
    led1_off()      - LED1 off
    led2_on()       - LED2 on
    led2_off()      - LED2 off
    leds_on()       - LED1, LED2 on
    leds_off()      - LED1, LED2 off
    led1_adjust()   - change LED1 PWM
    led2_adjust()   - change LED2 PWM
        ''')

    def led1_on( self ):
        GPIO.output( self.pin[0], True )

    def led2_on( self ):
        GPIO.output( self.pin[1], True )

    def leds_on( self ):
        GPIO.output( self.pin, True)

    def led1_off( self ):
        GPIO.output( self.pin[0], False )

    def led2_off( self ):
        GPIO.output( self.pin[1], False )

    def leds_off( self ):
        GPIO.output( self.pin, False)

    def led1_adjust( self, change ):
        self.AD1.start(100)
        if change == 'up':
            if self.brightness1 < 100:
                self.brightness1 += 10
        elif change == 'down':
            if self.brightness1 > 0:
                self.brightness1 -= 10
        self.AD1.ChangeDutyCycle(self.brightness1)

    def led2_adjust( self, change ):
        self.AD2.start(100)
        if change == 'up':
            if self.brightness2 < 100:
                self.brightness2 += 10
        elif change == 'down':
            if self.brightness2 > 0:
                self.brightness2 -= 10
        self.AD2.ChangeDutyCycle(self.brightness2)

    def led_jog( self ):
        self.jog = JogSwitch()
        while True:
            dir = self.jog.check_jog()
            time.sleep(0.2)
            if dir == 'up':
                print(dir)
                self.led1_on()
            elif dir == 'down':
                print(dir)
                self.led2_on()
            elif dir == 'left' or dir == 'center':
                print(dir)
                self.leds_on()
            elif dir == 'right':
                print(dir)
                self.leds_off()

class DCMotor( GPIO_Base ):
    MOTOR_PIN = { 'm_pwm': 12, 'm_p' : 4, 'm_n' : 25 }

    def __init__( self ):
        super().__init__( self.MOTOR_PIN['m_pwm'] )
        super().__init__( self.MOTOR_PIN['m_p'] )
        super().__init__( self.MOTOR_PIN['m_n'] )
        super().set_output( self.MOTOR_PIN['m_pwm'] )
        super().set_output( self.MOTOR_PIN['m_p'] )
        super().set_output( self.MOTOR_PIN['m_n'] )
        self.EN = super().set_PWM( self.MOTOR_PIN['m_pwm'], 100 )
        self.EN.start(100)
        self.speed = 100
        self.duty = 0

    def explain( self ):
        print('''
< DCMotor >
    cw()            - set clockwise
    ccw()           - set counterclockwise
    stop()          - stop motor
    speed_up()      - speed up
    speed_down()    - speed down
    DCmotor_jog()   - up( speed up ), down( speed down )
                      left( clockwise ), right( counterclockwise )
                      center( stop )
                      ''')

    def cw( self ):
        GPIO.output( self.MOTOR_PIN['m_pwm'], True )
        GPIO.output( self.MOTOR_PIN['m_p'], True )
        GPIO.output( self.MOTOR_PIN['m_n'], False )

    def ccw( self ):
        GPIO.output( self.MOTOR_PIN['m_pwm'], True )
        GPIO.output( self.MOTOR_PIN['m_p'], False )
        GPIO.output( self.MOTOR_PIN['m_n'], True )

    def stop( self ):
        GPIO.output( self.MOTOR_PIN['m_pwm'], False )
        GPIO.output( self.MOTOR_PIN['m_p'], False )
        GPIO.output( self.MOTOR_PIN['m_n'], False )

    def speed_up( self ):
        if self.speed < 100:
            self.speed += 10
        return self.speed

    def speed_down( self ):
        if self.speed > 0:
            self.speed -= 10
        return self.speed

    def change_speed( self, duty ):
        self.EN.ChangeDutyCycle( duty )

    def DCmotor_jog( self ):
        self.jog = JogSwitch()
        while True:
            dir = self.jog.check_jog()
            time.sleep(0.2)
            if dir == 'up':
                print( 'speed: {0:3}'.format( self.speed ) )
                self.change_speed( self.speed_up() )
            elif dir == 'down':
                print( 'speed: {0:3}'.format( self.speed ) )
                self.change_speed( self.speed_down() )
            elif dir == 'left':
                print( 'cw' )
                self.cw()
            elif dir == 'right':
                print( 'ccw' )
                self.ccw()
            elif dir == 'center':
                print( 'stop' )
                self.stop()

class JogSwitch( GPIO_Base ):
    #jog  [ up, dn, lt, rt, cen]
    JOG = [  5,  6, 16, 20,  21]
    DIR = [ 'up', 'down', 'left', 'right', 'center']
    STAT = [  0,  0,  0,  0,  0]

    def __init__( self ):
        for x in self.JOG:
            super().__init__( x )
            super().set_input( x )

    def explain( self ):
        print('''
< JogSwitch >
    check_jog()     - return directions( 'up', 'down', 'left', 'right', 'center' )
                      ''')

    def check_jog( self ):
        while True:
            for i in range( 5 ):
                if GPIO.input( self.JOG[i] ):
                    return self.DIR[i]

class CharacterLCD( GPIO_Base ):
    LCD_RS  = 23
    LCD_RW  = 24
    LCD_E   = 26
    LCD_D4  = 17
    LCD_D5  = 18
    LCD_D6  = 27
    LCD_D7  = 22

    #define some device constants
    LCD_WIDTH   = 16
    LCD_CHR     = True
    LCD_CMD     = False

    LCD_LINE_1 = 0x80
    LCD_LINE_2 = 0xC0

    #Time constants
    E_PULSE = 0.0005
    E_DELAY = 0.0005

    def __init__( self ):
        super().__init__( self.LCD_RS )
        super().__init__( self.LCD_RW )
        super().__init__( self.LCD_E )
        super().__init__( self.LCD_D4 )
        super().__init__( self.LCD_D5 )
        super().__init__( self.LCD_D6 )
        super().__init__( self.LCD_D7 )
        super().set_output( self.LCD_E )
        super().set_output( self.LCD_RS )
        super().set_output( self.LCD_D4 )
        super().set_output( self.LCD_D5 )
        super().set_output( self.LCD_D6 )
        super().set_output( self.LCD_D7 )

    def explain( self ):
        print('''
< CharacterLCD >
    lcd_string( message )     - present message to CharacterLCD
                      ''')

    def lcd_print( self, text, line ):
        if line == 1:
            line = self.LCD_LINE_1
        elif line == 2:
            line = self.LCD_LINE_2
        self.lcd_init()
        self.lcd_string( text, line )
        print("lCD : " + text)

    def lcd_init( self ):
        #initialize display
        self.lcd_byte(0x33, self.LCD_CMD ) # 00110011 initialze
        self.lcd_byte(0x32, self.LCD_CMD ) # 00110010 initialze
        self.lcd_byte(0x06, self.LCD_CMD ) # 00000110 cursor move direction
        self.lcd_byte(0x0C, self.LCD_CMD ) # 00001101 display on cursor off blink off
        self.lcd_byte(0x28, self.LCD_CMD ) # 00101000 data length, number of lines, font size
        self.lcd_byte(0x01, self.LCD_CMD ) # 00000001 clear display
        time.sleep( self.E_DELAY )

    def lcd_byte( self, bits, mode ):
        GPIO.output( self.LCD_RS, mode )

        #High bits
        GPIO.output( self.LCD_D4, False )
        GPIO.output( self.LCD_D5, False )
        GPIO.output( self.LCD_D6, False )
        GPIO.output( self.LCD_D7, False )

        if bits & 0x10 == 0x10:
            GPIO.output( self.LCD_D4, True )
        if bits & 0x20 == 0x20:
            GPIO.output( self.LCD_D5, True )
        if bits & 0x40 == 0x40:
            GPIO.output( self.LCD_D6, True )
        if bits & 0x80 == 0x80:
            GPIO.output( self.LCD_D7, True )

        #Toggle 'Enable' pin
        self.lcd_toggle_enable()

        #Low bits
        GPIO.output( self.LCD_D4, False )
        GPIO.output( self.LCD_D5, False )
        GPIO.output( self.LCD_D6, False )
        GPIO.output( self.LCD_D7, False )

        if bits & 0x01 == 0x01:
            GPIO.output( self.LCD_D4, True )
        if bits & 0x02 == 0x02:
            GPIO.output( self.LCD_D5, True )
        if bits & 0x04 == 0x04:
            GPIO.output( self.LCD_D6, True )
        if bits & 0x08 == 0x08:
            GPIO.output( self.LCD_D7, True )

        #Toggle 'Enable' pin
        self.lcd_toggle_enable()

    def lcd_toggle_enable( self ):
        #Toggle enable
        time.sleep( self.E_DELAY )
        GPIO.output( self.LCD_E, True )
        time.sleep( self.E_PULSE )
        GPIO.output( self.LCD_E, False )
        time.sleep( self.E_DELAY )

    def lcd_string( self, message, line ):
        #send string to display
        message = message.ljust( self.LCD_WIDTH, " ")
        self.lcd_byte( line, self.LCD_CMD )
        for i in range( self.LCD_WIDTH ):
            self.lcd_byte( ord(message[i]), self.LCD_CHR )

class Ultrasonic( GPIO_Base ):
    TRIG = 0
    ECHO = 1

    def __init__( self ):
        super().__init__( self.TRIG )
        super().__init__( self.ECHO )
        super().set_output( self.TRIG )
        super().set_input( self.ECHO )
        GPIO.output( self.TRIG, False )
        time.sleep( 0.5 )
        self.sense = 'safe'

    def explain( self ):
        print('''
< Ultrasonic >
    check_distance()     - check distance and return state
                            (sense <= 10cm --> 'too_close')
                            (sense > 10cm  --> 'safe')
                      ''')

    def check_distance( self ):
        GPIO.output( self.TRIG, True )
        time.sleep( 0.00001 )
        GPIO.output( self.TRIG, False )

        while GPIO.input( self.ECHO ) == False :
            pulse_start = time.time()

        while GPIO.input( self.ECHO ) == True :
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17000
        distance = round( distance, 2 )
        if distance > 10.0:
            self.sense = 'safe'
        elif distance <= 10.0:
            self.sense = 'too_close'

        return self.sense

class Piezo( GPIO_Base ):
    MELODY = { 'DO':261, 'RE':294, 'MI':329, 'FA':349, 'SOL':390, 'LA':440, 'SI':493, 'DO2':523 ,'P':0}
    PIEZO = 13

    def __init__( self ):
        super().__init__( self.PIEZO )
        super().set_output( self.PIEZO )
        self.P = super().set_PWM( self.pin, 100 )

    def explain( self ):
        print('''
< Piezo >
    play_sound( scale, time )     - play scale for time
    -scale 'DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI', 'DO2'
    lalala()                      - play song
                      ''')

    def play_sound( self, scale, length ):
        self.P.ChangeFrequency( self.MELODY[scale] )
        time.sleep( length )

    def lalala( self ):
        self.P.start( 90 )
        self.play_sound( 'MI', 0.2 )
        self.play_sound( 'SOL', 0.2 )
        self.play_sound( 'MI', 0.2 )
        self.play_sound( 'RE', 0.2 )
        self.P.stop()
        time.sleep(0.7)
        self.P.start( 90 )
        self.play_sound( 'RE', 0.2 )
        self.play_sound( 'SOL', 0.2 )
        self.play_sound( 'RE', 0.2 )
        self.play_sound( 'DO', 0.2 )
        self.P.stop()
        time.sleep(0.7)
        self.P.start( 90 )
        self.play_sound( 'LA', 0.4 )
        self.play_sound( 'SOL', 0.8 )
        self.P.stop()
        time.sleep(0.7)
        self.P.start( 90 )
        self.play_sound( 'MI', 0.4 )
        self.play_sound( 'SOL', 1 )
        self.P.stop()


class PIR( GPIO_Base ):
    PIR = 24

    def __init__( self ):
        super().__init__( self.PIR )
        super().set_input( self.PIR )
        self.detector = 0

    def explain( self ):
        print('''
< PIR >
    check_move()     - check movement and return 1 or 0
                      ''')

    def check_move( self ):
        while True:
            if GPIO.input( self.PIR ) == True:
                self.detector = 1
                time.sleep( 0.1 )
            elif GPIO.input( self.PIR ) != True :
                self.detector = 0
                time.sleep(0.1)
            return self.detector

    def control_pir( self ):
        try:
            return self.check_move()
        except KeyboardInterrupt:
            pass
