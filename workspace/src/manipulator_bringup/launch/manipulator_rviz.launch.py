from launch import LaunchDescription
from launch_ros.actions import Node
import os 
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():
    ld = LaunchDescription()

    # fetch urdf files
    manipulator_simulation_pkg = get_package_share_directory("manipulator_simulation")
    urdf = os.path.join(manipulator_simulation_pkg,"urdf","manipulator.urdf")

    # call joint state publisher
    jointPub = Node(package="joint_state_publisher_gui",executable="joint_state_publisher_gui",name="joint_state_publisher_gui",arguments=[urdf])

    # call robot state publisher
    statePub = Node(package="robot_state_publisher",executable="robot_state_publisher",name="robot_state_publisher",output ="screen",arguments=[urdf])

    # call rviz gui
    rviz2 = Node(package="rviz2",executable = "rviz2",name = "rviz2",output = "screen")
    

    # add nodes
    ld.add_action(rviz2)
    ld.add_action(jointPub)
    ld.add_action(statePub)

    return ld