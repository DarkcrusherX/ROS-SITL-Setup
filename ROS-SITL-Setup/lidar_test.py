import rospy
from sensor_msgs.msg import LaserScan

rospy.init_node('lidar_example', anonymous=True)

def lidar_callback(lidar_msg):
  rospy.loginfo(lidar_msg.header)
  print(len(lidar_msg.ranges))
  print(lidar_msg.ranges[0])

sub_lidar = rospy.Subscriber("/spur/laser/scan", LaserScan, lidar_callback)

rospy.spin()