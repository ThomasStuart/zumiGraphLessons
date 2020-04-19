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

# ex 1:
# currHeading    = 270  (down)
# desiredHeading = 90   (up)
# X = 180
# we want to turn 180 degrees in the pos -> turning left by 180 

# answer = change_heading_to_desired_heading(currHeading, desiredHeading ) 
# answer = 90 

def change_heading_to_desired_heading( currHeading, desiredHeading):
        # step1: calc the magnitude of angle change , call it X
        X = currHeading - desiredHeading
        
        #step2: determine which way we need to turn
        if  X    >    0:
            print("turned left")
            zumi.turn_left( X )
            return desiredHeading
        
        elif X   <    0:
            X = abs( X )
            print("turned right")
            zumi.turn_right( X )
            return desiredHeading
        
        else:
            print( "no turn needed ")
            return desiredHeading
    

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


