import rospy

from trajectory_msgs.msg import JointTrajectory
from trajectory_msgs.msg import JointTrajectoryPoint
from std_msgs.msg import Float64




def talker :
    pub = rospy.Publisher('JTP', JointTrajectory , queue_size=10)
    rospy.init_node('jtptalk', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        msg1=JointTrajectory()
        jtp=JointTrajectoryPoint()
        msg1.joint_names = ["joint1"]
        jtp.positions =[0.5]
        jtp.time_from_start = [1,0]
        msg1.points.append(jtp)
        rospy.loginfo(msg1)
        pub.publish(msg1)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass