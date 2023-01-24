# Manipulator Robot Simulation
It is a simple manipulator robot with a forward kinematics controller buildt in with the ros2 control framework and a service to publish the desired position.


# Usage
### Start the docker container
```
./docker_run.sh
```
### Spawn additional terminals
```
docker exec -it ros2_container bash
```
### Publish a joint's desired position
Substitute with desired position for each actuator joint:
```
ros2 service call /controller_service manipulator_interfaces/srv/ManipulatorForwardKinematicsTargets "{joint_1_target: -1.56, joint_2_target: 0.2, joint_4_target: 0.2}"
```
