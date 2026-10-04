"""Start the Workshop 2 world and connect it to ROS 2.

Run with:  ros2 launch sim/sim.launch.py
"""
import os

from launch import LaunchDescription
from launch.actions import ExecuteProcess
from launch_ros.actions import Node

WORLD = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'workshop.sdf')


def generate_launch_description():
    # Gazebo Fortress: -r starts the simulation running instead of paused
    gazebo = ExecuteProcess(cmd=['ign', 'gazebo', '-r', WORLD], output='screen')

    # ROS 2 <-> Gazebo bridge
    #   ]  = ROS 2 -> Gazebo   (our drive commands)
    #   [  = Gazebo -> ROS 2   (odometry back to us)
    bridge = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/cmd_vel@geometry_msgs/msg/Twist]ignition.msgs.Twist',
            '/odom@nav_msgs/msg/Odometry[ignition.msgs.Odometry',
        ],
        output='screen',
    )

    return LaunchDescription([gazebo, bridge])
