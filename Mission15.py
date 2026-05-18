from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

hub = PrimeHub()
left_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C)
attachment_motor = Motor(Port.A)
attachment_motor2 = Motor(Port.E, gears=[12, 36])
drive_base =  DriveBase(left_motor,right_motor,wheel_diameter=56, axle_track=142)
drive_base.use_gyro(True)
drive_base.settings(straight_speed= 550, straight_acceleration=650)
drive_base.settings(turn_rate= 400, turn_acceleration=650)

drive_base.straight(150)
drive_base.turn(80)
drive_base.straight(610)
drive_base.turn(-57)

#attachment_motor2.run_until_stalled(-50, duty_limit=50)
#attachment_motor2.reset_angle(0)
attachment_motor2.run_angle(10000,103)
drive_base.settings(straight_acceleration=500,straight_speed=500)
drive_base.straight(587)
attachment_motor2.run_angle(10000,-75)
drive_base.straight(-537)
drive_base.turn(-100)
attachment_motor2.run_angle(500,140)

