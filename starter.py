from zumi.zumi import Zumi

zumi = Zumi()
zumi.mpu.calibrate_MPU()

# CONSTANTS
DIV_CONST = 6.0
POWER = 40

def getTimeForTravel(dist):
    time = (dist + 1) / DIV_CONST
    return time


#make zumi go left by 10  inches from point S to point A
distanceInInches = 10
timeToTravel = getTimeForTravel(distanceInInches)
zumi.turn_left(90)
zumi.forward( POWER, timeToTravel)

#write the code to get Zumi  from point S to point X

#write the code to get Zumi  from point S to point B


#goal is to type in X instead of 10  from point S
#  travel('s', 'x')
#  travel('x', 'a')
