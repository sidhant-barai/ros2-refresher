#!/usr/bin/env/ python3
import rclpy
from rclpy.node import Node
from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtle_contoller")
        self.cmd_vel_publ_ = self.create_publisher(Twist, "/turtle1/cmd_vel", 10)
        self.pose_sub_ = self.create_subscription(Pose, "/turtle1/pose", self.callback_pos, 10)

    def callback_pos(self, pose: Pose):
        cmd = Twist()
        if pose.x < 5.5:
            cmd.linear.x = 1.0
            cmd.angular.z - 1.0
        else:
            cmd.linear.x = 2.0
            cmd.angular.z - 2.0
        self.cmd_vel_publ_.publish(cmd)
        

def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutown()

if __name__ == '__main__':
    main()