#!/usr/bin/env python
#For Raspberry Pi2

import rospy
from std_msgs.msg import String

def callback(message):
    rospy.loginfo("%s",message.data)

rospy.init_node('PlayMusicRobot')
sub = rospy.Subscriber('HandOff',String,callback)
rospy.spin()
