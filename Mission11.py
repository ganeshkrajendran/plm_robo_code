from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch, run_task, multitask

hub = PrimeHub()
left_motor = Motor(Port.D, Direction.COUNTERCLOCKWISE)
right_motor = Motor(Port.C)
attachment_motor = Motor(Port.A, gears=[12, 20])
attachment_motor2 = Motor(Port.E, gears=[12, 20])
drive_base =  DriveBase(left_motor,right_motor,wheel_diameter=56, axle_track=142)
drive_base.use_gyro(True)

drive_base.settings(straight_speed= 700, straight_acceleration=700)
drive_base.settings(turn_rate= 350, turn_acceleration=350)
# actual code for mission 11
drive_base.straight(735)
drive_base.settings(straight_acceleration=900)
drive_base.turn(-75)
drive_base.straight(58)
drive_base.turn(-18)
attachment_motor.run_angle(15000,1800)
drive_base.straight(-100)
drive_base.turn(110)

# mission 13 starts here.
# building to validate 

#attachment_motor2.run_until_stalled(100, duty_limit=50)
#attachment_motor2.reset_angle(0)
#drive_base.straight(100)
#drive_base.turn(20)
#attachment_motor2.run_angle(2000,-460)
#drive_base.straight(140)
#attachment_motor2.run_angle(2000, 80, then=Stop.HOLD, wait=True)
#wait(1000)
#drive_base.turn(30) 
#drive_base.turn(-95)
#attachment_motor2.run_angle(4000,200)
#drive_base.straight(700)

# Use a global variable to track if the arm is done
arm_is_ready = False

async def reset_arm():
    global arm_is_ready
    # 1. Reset the arm in the background
    await attachment_motor2.run_until_stalled(100, duty_limit=50)
    attachment_motor2.reset_angle(0)
    
    # 2. Signal that the arm is now free to use
    arm_is_ready = True
    print("Arm reset! Drive mission can now use the motor.")

async def drive_mission():
    # These movements use the WHEELS (no conflict yet)
    await drive_base.straight(105)
    await drive_base.turn(16)
    
    # --- CRITICAL CHECK ---
    # This loop pauses the drive mission UNTIL reset_arm is finished
    #while not arm_is_ready:
    #    await wait(10) 
    
    # Now it is safe to use the attachment motor!
    await attachment_motor2.run_angle(2000, -260)
    await drive_base.straight(130)
    await drive_base.turn(-5)
    await attachment_motor2.run_angle(2000, 80, then=Stop.HOLD, wait=True)
    
    await wait(500)
    await drive_base.turn(30)
    await drive_base.straight(-25)
    await attachment_motor2.run_angle(4000, 200)
    await drive_base.turn(-80)
    await drive_base.straight(750)
    
    

async def main():
    # This line runs BOTH functions at the exact same time.
    # The program only moves past this line once BOTH are finished.
    await multitask(drive_mission())

run_task(main())







#drive_base.straight(-100)
#drive_base.settings(turn_rate= 400, turn_acceleration=350)
#drive_base.turn(130)
#drive_base.straight(210)
#attachment_motor2.run_angle(4000, 125, then=Stop.HOLD, wait=True)
#wait(1000)
#drive_base.turn(30)
#drive_base.straight(-90)
#drive_base.turn(-30)
