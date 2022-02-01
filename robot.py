from matplotlib.pyplot import cla
from sr.robot3 import *
R = Robot()
print("hello world")
import time 
POWER = 1
#R.power.beep(100, note="c")
#R.power.beep(100, note="c")
def move_forward():
    R.motor_board.motors[0].power = POWER
    time.sleep(10)
    
move_forward()
#R.power.beep(100, note="c")
move_forward()
#R.power.beep(100, note="d")



class Movement():
    def __init__(self, R, motorboard1, motorboard2):
        self.R = R
        self.fb = motorboard1
        self.bb = motorboard2
        self.fb_l_power = 0
        self.fb_r_power = 0
        self.bb_l_power = 0
        self.bb_r_power = 0
    
    def move(self):
        self.R.motor_boards[self.fb].motors[0].power = self.fb_l_power
        self.R.motor_boards[self.fb].motors[1].power = self.fb_r_power
        self.R.motor_boards[self.bb].motors[0].power = self.bb_l_power
        self.R.motor_boards[self.bb].motors[1].power = self.bb_r_power
    
    def forwards(self):
        self.fb_l_power = 1
        self.fb_r_power = 1
        self.bb_l_power = 1
        self.bb_l_power = 1
        self.move()

    def backwards(self):
        self.fb_l_power = -1
        self.fb_r_power = -1
        self.bb_l_power = -1
        self.bb_l_power = -1
        self.move()

    def left(self):
        self.fb_l_power = 1
        self.fb_r_power = -1
        self.bb_l_power = -1
        self.bb_l_power = 1
        self.move()

    def right(self):
        self.fb_l_power = -1
        self.fb_r_power = 1
        self.bb_l_power = 1
        self.bb_l_power = -1
        self.move()

    def start(self):
        self.forwards()
        time.sleep(5)
        self.backwards()
        time.sleep(5)
        self.left()
        time.sleep(5)
        self.right()
        time.sleep(5)



def main():
    R = Robot()
    motorboard1 = 'serial' #Front motorboard
    motorboard2 = 'serial' #Back motorboard
    robo = Movement(R, motorboard1, motorboard2)
    robo.start()



if __name__ == '__main__':
    main()