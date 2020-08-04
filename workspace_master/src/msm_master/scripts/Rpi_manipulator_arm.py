#!/usr/bin/env python
import rospy
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from std_msgs.msg import Float64
import math




def subs():
    rospy.init_node('armmove', anonymous=True)
    rospy.Subscriber('/arm_controller/command' , JointTrajectory , Callback )
    rospy.spin()

def Callback(data):
    angles = data.points[0].positions
    anglesindeg = [1,2,3,4]
    anglesinposdeg = [1,2,3,4,90]
    anglesindeg[0] = int(math.degrees(angles[0]))
    anglesindeg[1] = int(math.degrees(angles[1]))
    anglesindeg[2] = int(math.degrees(angles[2]))
    anglesindeg[3] = int(math.degrees(angles[3]))
    for i in range(0,4):
        if (anglesindeg[i]<0):
            anglesinposdeg[i]=(anglesindeg[i]*-1)+90
        else:
            anglesinposdeg[i]=anglesindeg[i]
    
    rospy.loginfo(anglesinposdeg)

if __name__=='__main__':
    subs()
    
    

