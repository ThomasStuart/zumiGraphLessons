from zumi.zumi import Zumi
zumi = Zumi()

# CONSTANTS
DIV_CONST = 6.0
POWER   = 40
# globals
heading = 0
route = [ (90, 10) ] # first part is angle, second is distance 
                        # angle = 90  , distance = 10
    
def getTimeForTravel(distanceInInches):
    time = (distanceInInches + 1) / DIV_CONST
    return time

    
def change_angle_to_desired( currHeading, desiredHeading):
    zumi.turn_left(90)
    return 90
    
while len( route ) != 0 :
    pair = route[0]
    
    desired_angle    = pair[0]
    desired_distance = pair[1]
    
    
    #write some fx to change the angle to desired one
    heading = change_angle_to_desired( heading, desired_angle )
    
    time = getTimeForTravel(desired_distance)
    zumi.forward(POWER, time)
    
    route.pop(0)


