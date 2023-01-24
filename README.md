# Manipulator Robot Simulation
It is a simple manipulator robot with a forward kinematics controller buildt in with the ros2 control framework and a service to publish the desired position.


# Usage
### Start the docker container
```
./docker_run.sh
```
#### IMPORTANT NOTE
The ROS2 ControllerManager breaks two important scripts when the dependency is installed from package inside a docker container image. This can be solved by running ```./fix_controller.sh``` in addition to the normal ros source (```source install/setup.bash```)

### Spawn additional terminals
```
docker exec -it ros2_container bash
```
### Start the Controller:
```
ros2 launch manipulator_bringup manipulator_controller_bringup.launch.py 

```
### Publish a joint's desired position
Substitute with desired position for each actuator joint:
```
ros2 service call /controller_service manipulator_interfaces/srv/ManipulatorForwardKinematicsTargets "{joint_1_target: -1.56, joint_2_target: 0.2, joint_4_target: 0.2}"
```
