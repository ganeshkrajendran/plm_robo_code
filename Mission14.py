from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask

hub = PrimeHub()
hub = PrimeHub()
left_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C)
attachment_motor = Motor(Port.A, gears=[12, 20])
attachment_motor2 = Motor(Port.E, gears=[12, 20])
drive_base =  DriveBase(left_motor,right_motor,wheel_diameter=56, axle_track=142)
drive_base.use_gyro(True)


drive_base.settings(straight_speed= 700, straight_acceleration=700)
drive_base.settings(turn_rate= 350, turn_acceleration=350)
drive_base.straight(200)
drive_base.turn(48)
drive_base.straight(250)
drive_base.straight(-250)
drive_base.turn(-46)
drive_base.straight(-200)

