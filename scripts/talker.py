#!/usr/bin/env python
import rospy
from std_msgs.msg import String

rospy.init_node('talker')
pub = rospy.Publisher('chatter',String,queue_size=10)
rate = rospy.Rate(10)
while not rospy.is_shutdown():
    Music = String()
    Music.data = "hello world %s" % rospy.get_time()
    pub.publish(Music)
    rate.sleep()
