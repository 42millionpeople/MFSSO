#!/usr/bin/env pybricks-micropython
# DONT DELETE LINE 1
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# Initialize the EV3 Brick.
ev3 = EV3Brick()
# Most values are in Hz, ms, or mm
ev3.speaker.beep(frequency=100, duration=500)
ev3.speaker.beep(frequency=500, duration=500)
lmotor = Motor(Port.A)
rmotor = Motor(Port.B)
# Setting drive train - must be changed for every surface and bot design
drive = DriveBase(lmotor, rmotor, wheel_diameter=56, axle_track=116)
# ^^ wheel diameter is ~50mm, but set to 56 mm to account for error. 
# Axle track is distance between wheel centers and has also been adjusted.
# drive.drive(100, 80)
# drive.straight(300)
# for x in range(30):
#     drive.straight(100)
#     drive.turn(90)
# ^^ random testing for accuracy and tuning

def go(dist):
    drive.straight(dist*500)
def tgo(deg,dist):
    drive.turn(deg*92)
    go(dist)
def tar():
   drive.turn(184)
drive.straight(350)
go(1)
tgo(-1,1)
for i in range(4):
    tgo(1,1)


#STR8 = 4 SE
#TURN = .75 ISH SUCESSKECNUNDO

