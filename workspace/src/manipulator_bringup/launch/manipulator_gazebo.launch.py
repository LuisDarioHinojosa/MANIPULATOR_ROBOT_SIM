
import os 
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
from scripts import GazeboRosPaths
from ament_index_python.packages import get_package_share_directory

def generate_launch_description():
    ld = LaunchDescription()
    # urdf
    manipulator_simulation_pkg = get_package_share_directory("manipulator_simulation")
    urdf = os.path.join(manipulator_simulation_pkg,"urdf","manipulator.urdf")
    # gazebo
    model_path, plugin_path, media_path = GazeboRosPaths.get_paths()
    gazebo_env = {
        "GAZEBO_MODEL_PATH":model_path,
        "GAZEBO_PLUGIN_PATH":plugin_path,
        "GAZEBO_RESOURCE_PATH":media_path
    }
    # create gazebo process (call gazebo)
    gazebo_cmd = ExecuteProcess(cmd=["gazebo","-s","libgazebo_ros_factory.so"],output="screen",additional_env=gazebo_env)
    
    # create gazebo node (bring robot into gazebo)
    gazebo_node = Node(package="gazebo_ros",executable="spawn_entity.py",arguments=["-entity","manipulator_robot","-b","-file", urdf])
    # call robot state publisher
    state_pub_node = Node(package="robot_state_publisher",executable="robot_state_publisher",name="robot_state_publisher",output ="screen",arguments=[urdf])

    # add nodes
    ld.add_action(gazebo_cmd)
    ld.add_action(gazebo_node)
    ld.add_action(state_pub_node)

    return ld