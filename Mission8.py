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
drive_base.settings(straight_speed= 900, straight_acceleration=900)
drive_base.settings(turn_rate= 300, turn_acceleration=650)

drive_base.straight(220)
attachment_motor2.run_angle(10000, 180)
attachment_motor2.run_angle(10000, -130)
#drive_base.straight(40)
#Mission 8

    
# 2. Immediately start the flapping once zero is found
for _ in range(3):
    attachment_motor2.run_angle(10000, 130)
    attachment_motor2.run_angle(10000, -130)

#Mission 9 and 10                               
drive_base.straight(-130)
drive_base.turn(-36)
drive_base.straight(300)
attachment_motor.run_angle(10000, 420)
drive_base.straight(-130)
attachment_motor.run_angle(10000, -20)

drive_base.straight(40)
attachment_motor.run_angle(10000, -300)
drive_base.straight(83)
drive_base.turn(-43)
drive_base.straight(-30)

drive_base.turn(45)

drive_base.straight(-155)
drive_base.turn(-30)

drive_base.straight(137)
attachment_motor.run_angle(1000, 300)

drive_base.turn(-20)
drive_base.straight(-450)
drive_base.turn(-30)
