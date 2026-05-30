from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
left_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C)
attachment_motor = Motor(Port.A)
attachment_motor2 = Motor(Port.E)
drive_base =  DriveBase(left_motor,right_motor,wheel_diameter=56, axle_track=142)
drive_base.use_gyro(True)
drive_base.settings(straight_speed= 800)
drive_base.settings(turn_rate= 100)

drive_base.straight(100)
drive_base.turn(-26)
drive_base.straight(200)
drive_base.turn(25)
drive_base.straight(310)
drive_base.turn(50)
drive_base.straight(80)
attachment_motor.run_angle(7000, 340)
drive_base.straight(65)
attachment_motor.run_angle(500,-340)
drive_base.straight(-10)
attachment_motor2.run_angle(7000,120)
wait(500)
drive_base.straight(-135)
drive_base.turn(-45)
drive_base.straight(15)
drive_base.turn(-45)
drive_base.straight(-70)
drive_base.turn(-155)
drive_base.straight(525)