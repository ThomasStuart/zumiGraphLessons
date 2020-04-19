from zumi.zumi import Zumi
zumi = Zumi()

# CONSTANTS
DIV_CONST = 6.0
POWER   = 40
# globals
heading = 0   
route = [ (90, 10) ] # first part is angle, second is distance 
                        # angle = 90 degrees , distance = 10 inches 
    
def getTimeForTravel(distanceInInches):
    time = (distanceInInches + 1) / DIV_CONST
    return time

def change_heading_to_desired_heading( currHeading, desiredHeading):
    zumi.turn_left(90)
    return 90
    

# GOAL IS TO GET TO AN EMPTY LIST
# start > 0 but end at 0 

while len( route ) != 0 :
    pair = route[0]  # pair = (90, 10)
    
    desired_angle    = pair[0]  # 90
    desired_distance = pair[1]  # 10
    
    # Step1: change heading to desired heading 
    change_heading_to_desired_heading( heading, desired_angle )
   
    
    # Step2: get the distance we need to go 
    time = getTimeForTravel(desired_distance)
    zumi.forward(POWER, time)
    
    
    # Step3: deletes the first element in list
    route.pop(0)


