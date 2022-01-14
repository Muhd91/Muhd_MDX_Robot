#!/usr/bin/env python


import rospy
from nav_msgs.msg import Odometry
from tf.transformations import euler_from_quaternion
from geometry_msgs.msg import Point, Twist
from math import atan2


x = 0.0
y = 0.0
theta = 0.0

def newOdom (msg):
    global x
    global y
    global theta

    x = msg.pose.pose.position.x
    y = msg.pose.pose.position.y
    
    rot_q = msg.pose.pose.orientation
    (roll, pitch, theta) = euler_from_quaternion ([rot_q.x, rot_q.y, rot_q.z, rot_q.w])


rospy.init_node ("speed_controller")

sub = rospy.Subscriber("/odometry/filtered", Odometry, newOdom)
pub = rospy.Publisher("/cmd_vel",Twist, queue_size=1)

speed = Twist()

r = rospy.Rate(4)


goal = Point ()
goal.x = 2
goal.y = 2

while not rospy.is_shutdown():

    inc_x = goal.x - x
    inc_y = goal.y - y

    angle_to_goal = atan2 (inc_y,inc_x)


    if abs(angle_to_goal - theta) > 1:
        speed.linear.x = 0.0
        speed.angular.z = 0.1

    else if:
        goal.x = 3
        goal.y = 4
        abs(angle_to_goal - theta) > 1:
        speed.linear.x = 0.0
        speed.angular.z = 0.1
    else if:
        goal.x = -1
        goal.y = -1
        abs(angle_to_goal - theta) > 1:
        speed.linear.x = 0.0
        speed.angular.z = 0.1
    else
        speed.linear.x = 1.0
        speed.angular.z = 0.0


    pub.publish(speed)
    r.sleep()




