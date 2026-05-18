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
drive_base.settings(straight_speed=900)
drive_base.settings(turn_rate=200)
drive_base.straight(415)
attachment_motor2.run_angle(1000, 430)
drive_base.straight(-100)
attachment_motor2.run_angle(1000,-410)
drive_base.straight(200)
drive_base.straight(-70)
drive_base.turn(7)
attachment_motor.run_angle(700,-380)
attachment_motor.run_angle(700, 200)
drive_base.settings(straight_speed=950, straight_acceleration=2000)
drive_base.straight(-500)

