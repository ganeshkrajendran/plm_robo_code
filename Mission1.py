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
drive_base.settings(straight_speed= 600, straight_acceleration=600)
drive_base.settings(turn_rate= 400, turn_acceleration= 400)



drive_base.straight(555)
drive_base.turn(-87)
drive_base.straight(-50)

attachment_motor.run_until_stalled(20, duty_limit=-20)
attachment_motor.reset_angle(0)


attachment_motor.run_angle(2000, -330)
wait(500)

drive_base.straight(50)
attachment_motor.run_angle(7000, 300)

drive_base.straight(-70)
drive_base.turn(40)
attachment_motor2.run_angle(1000, 94)
drive_base.settings(straight_speed=100)
drive_base.straight(217)
attachment_motor2.run_angle(10000, -50)
drive_base.turn(-10)
drive_base.settings(straight_speed=900)
drive_base.straight(-185)
drive_base.turn(-105)

drive_base.straight(620)