#!/bin/bash
target_path=/opt/ros/humble/lib/controller_manager

cat $target_path/spawner >> $target_path/spawner.py

cat $target_path/unspawner >> $target_path/unspawner.py

chmod u+x $target_path/spawner.py $target_path/unspawner.py