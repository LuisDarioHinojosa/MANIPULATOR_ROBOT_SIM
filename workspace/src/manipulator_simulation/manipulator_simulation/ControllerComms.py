#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from builtin_interfaces.msg import Duration
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
from manipulator_interfaces.srv import ManipulatorForwardKinematicsTargets

class ControllerComms(Node): 
    def __init__(self):
        super().__init__("controller_comms_node") 

        # declare parameters
        self.declare_parameter("joint_trayectory_controller_node","/joint_trajectory_controller/joint_trajectory")
        self.declare_parameter("publish_buffer_size",10)
        self.declare_parameter("controller_service_name","controller_service") 

        # fetch parameters
        controller_topic = self.get_parameter("joint_trayectory_controller_node").value
        buffer_size = self.get_parameter("publish_buffer_size").value
        controller_service_name = self.get_parameter("controller_service_name").value

        # fixed actuated joints (robot structure)
        self.joints = ["joint_1","joint_2","joint_4"]

        # create publisher and service
        self.trajectory_publisher = self.create_publisher(JointTrajectory,controller_topic,buffer_size)
        self.service = self.create_service(ManipulatorForwardKinematicsTargets,controller_service_name,self.service_callback)
        self.get_logger().info("CONTROLLER COMMUNICATION SERVER ONLINE")

    def service_callback(self,request,response):
        # update targets
        target_goals = [request.joint_1_target,request.joint_2_target,request.joint_4_target]
        # move the robot
        trajectory_msg = JointTrajectory()
        trajectory_msg.joint_names = self.joints
        point = JointTrajectoryPoint()
        point.positions = target_goals
        point.time_from_start = Duration(sec = 2)
        trajectory_msg.points.append(point)
        self.trajectory_publisher.publish(trajectory_msg)
        response.response = True
        return response
 
def main(args=None):
    rclpy.init(args=args)
    node = ControllerComms()
    rclpy.spin(node)
    rclpy.shutdown()
 
 
if __name__ == "__main__":
    main()