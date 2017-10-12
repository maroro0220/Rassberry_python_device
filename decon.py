
import team1_GPIO as gp
import team1_I2C as i2c
class DV_Con:
      def __init__(self):
            self.rl=gp.LED()
      def conGP(self,data):
          if data=='l1_on':
              self.rl.led1_on()
          elif data=='l2_on':
              self.rl.led_on(15)
if __name__=='__main__':
    dc=DV_Con()
