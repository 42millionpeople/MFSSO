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
ev3.speaker.beep(frequency=2000, duration=500)
ev3.speaker.beep(frequency=1000, duration=500)
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
def gocm(dist):
    drive.straight(dist*10)

gocm(10)
