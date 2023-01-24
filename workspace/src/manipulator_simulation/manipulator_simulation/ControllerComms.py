#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from builtin_interfaces.msg import Duration
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
 
class ControllerComms(Node): 
    def __init__(self):
        super().__init__("controller_comms_node") 

        # declare parameters
        self.declare_parameter("joint_trayectory_controller_node","/joint_trajectory_controller/joint_trajectory")
        self.declare_parameter("timer_period",10)
        self.declare_parameter("publish_buffer_size",10)

        # fetch parameters
        controller_topic = self.get_parameter("joint_trayectory_controller_node").value
        timer_period = self.get_parameter("timer_period").value
        buffer_size = self.get_parameter("publish_buffer_size").value
        
        # fixed actuated joints (robot structure)
        self.joints = ["joint_1","joint_2","joint_4"]
        self.target_goal = [1.57,0.50,1.2]

        # create publisher and timer
        self.trajectory_publisher = self.create_publisher(JointTrajectory,controller_topic,buffer_size)
        self.timer = self.create_timer(timer_period,self.timer_callback)

        self.get_logger().info("CONTROLLER COMMUNICATION NODE ONLINE")

    def timer_callback(self):
        trajectory_msg = JointTrajectory()
        trajectory_msg.joint_names = self.joints
        point = JointTrajectoryPoint()
        point.positions = self.target_goal
        point.time_from_start = Duration(sec = 2)
        trajectory_msg.points.append(point)
        self.trajectory_publisher.publish(trajectory_msg)
 
 
def main(args=None):
    rclpy.init(args=args)
    node = ControllerComms()
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()