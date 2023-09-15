from djitellopy import Tello
import cv2
import time

########################################################################
width = 320
height = 240
startCounter = 1
########################################################################

# connect Tello drone
me = Tello()
me.connect()
me.for_back_velocity = 0
me.left_right_velocity = 0
me.up_down_velocity = 0
me.yaw_velocity = 0
me.speed = 0

me.streamoff()
me.streamon()

while True:
    # get battery
    batt = me.get_battery()
    
    # Get stream from tello
    frame_read = me.get_frame_read()
    myframe = frame_read.frame
    img = cv2.resize(myframe, (width, height))
    
    # To go up in the beginning
    if startCounter == 0:
        me.takeoff()
        time.sleep(5)
        me.move_left(20)
        time.sleep(5)
        me.rotate_clockwise(90)
        time.sleep(5)
        # me.land()
        startCounter = 1
    
    # Send Velocity Value  to tello
    if me.send_rc_control:
        me.send_rc_control(me.left_right_velocity, me.for_back_velocity, me.up_down_velocity, me.yaw_velocity)
    
    # display the stream
    cv2.putText(myframe, f"Battery: {batt}", (110, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 3)
    cv2.imshow("stream", myframe)
    
    # wait for the key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        me.land()
        break

cv2.destroyAllWindows()

