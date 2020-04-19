heading = 0
POWER = 40 
route = [ (90, 10) ]   # LENGTH == 1 
#route = [ (90, 10) , (180, 10), (270, 10) ]   # LENGTH == 3 

def getTimeForTravel(distanceInInches):
    time = (distanceInInches + 1) / DIV_CONST
    return time



def change_angle_to_desired ( curr_heading , desired_angle ):    
    # step 1: alpha <- calculate the distance to turn
    alpha = curr_heading -  desired_angle
    
    # turn left is positve  
    if alpha > 0:
        zumi.turn_left( alpha ) 
        return desired_angle  # return the angle angle we will be heading at 

    # turn right is negative 
    elif alpha < 0:
        # HOW Do I FORCE ALPHA TO BE POS WITH ABS FUNCTION 
        alpha = abs(alpha) 
        zumi.turn_right( alpha )
        return desired_angle  # return the angle angle we will be heading at 
    else:
        # not gonna turn, already there
        return desired_angle  # return the angle angle we will be heading at 
        


while ( len(route) != 0 ):
    angle_dist = route[0]

    desired_angle = angle_dist[0]
    desired_dist  = angle_dist[1] # always be 10 for now

    # Step 1: change Zumi's angle
    change_angle_to_desired( heading, desired_angle ) 
    
    # Step 2: have zumi go for 10 inches
    time = getTimeForTravel(desired_dist)
    zumi.forward(POWER, time)

    
    #DELETE the edge we just took
    route.pop(0)

