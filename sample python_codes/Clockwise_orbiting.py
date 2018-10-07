import math
def clockwise_orbiting(x_coordinate,y_coordinate,time,radius,ang_velocity):
    theta=math.atan(y_coordinate/x_coordinate)
    new_x_coordinate=radius*math.cos(theta-ang_velocity*time)
    new_y_coordinate=radius*math.sin(theta-ang_velocity*time)
    return (new_x_coordinate,new_y_coordinate)

'''x=0
while(x<11):
    print(clockwise_orbiting(1,1.7321,x,1,5))
    x=x+0.01
'''