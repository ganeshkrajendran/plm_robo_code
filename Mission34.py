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

drive_base.settings(straight_speed= 650, straight_acceleration=650)
drive_base.settings(turn_rate= 300, turn_acceleration=300)


drive_base.straight(700)
drive_base.turn(40)
drive_base.straight(155)
drive_base.turn(48)
drive_base.straight(-50)
attachment_motor.run_angle(7000, 325)
attachment_motor2.run_angle(7000, 350)
drive_base.settings(straight_speed= 50)
drive_base.straight(95)
attachment_motor2.run_angle(200, -270)
attachment_motor.run_angle(100,-70)
drive_base.turn(2)
drive_base.straight(-114)
drive_base.settings(straight_speed= 950)
attachment_motor.run_angle(300,-200)
drive_base.straight(70)
drive_base.turn(100)
drive_base.straight(780)