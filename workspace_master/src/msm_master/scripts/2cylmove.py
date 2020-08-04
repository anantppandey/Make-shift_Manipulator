#!/usr/bin/env python
import rospy
from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from std_msgs.msg import Float64

global msg1



def main():
    pub=rospy.Publisher('/arm_controller/command' , JointTrajectory , queue_size=5)
    rospy.init_node('cylmove', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        #inp=raw_input("enter the direc: ")
        #inps=str(inp)

        lst =[] 
        
       # if inps=="w":
            
        n = 4       # int(input("Enter number of elements : ")) 
        for i in range(0, n):
            print "Enter the Position for joint-" 
            print i+1 
            ele = float(input())
            lst.append(ele)

        joint=['joint1' , 'joint2' , 'joint3' , 'joint4']
        msg1=JointTrajectory()
        msg1.joint_names=joint
        msg1.header.seq = 0

            #msg1.header.stamp =rospy.Time.now()  
              
        jtp=JointTrajectoryPoint()
        jtp.positions=lst
       # jtp.velocities = [0.1]
        #jtp.accelerations = [0.0]
        #jtp.effort = [0.0]
        jtp.time_from_start = rospy.Duration.from_sec(1.01)


        msg1.points.append(jtp)
        pub.publish(msg1)
        rospy.loginfo(msg1)
            
        rate.sleep()


if __name__=='__main__':
    main()