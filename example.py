#!/usr/bin/env python3

# Example: Move the turtle forward a set distance, then stop.
# To start this node open a new terminal and run:
#   python3 move_turtle.py
# Make sure turtlesim is running first though!!!

import time
import rclpy
from geometry_msgs.msg import Twist

def move_turtle(linear_speed, distance):
    # Build the velocity command
    move_cmd = Twist()
    move_cmd.linear.x = linear_speed
    move_cmd.angular.z = 0.0

    # How long to drive:  time = distance / speed
    time_duration = distance / linear_speed
    rate_hz = 200 # publish 200 times per second

    node.get_logger().info(
        f"Moving forward {distance} meters at {linear_speed} m/s..."
    )

    # Keep publishing until enough time has passed
    start_time = time.time()
    while time.time() - start_time < time_duration:
        pub.publish(move_cmd)
        time.sleep(1.0 / rate_hz)

    # Stop the turtle
    move_cmd.linear.x = 0.0
    pub.publish(move_cmd)
    node.get_logger().info("Turtle has stopped moving.")


if __name__ == '__main__':
    # Start ROS 2 and create our node
    rclpy.init()
    node = rclpy.create_node('move_turtle_node')

    # Publisher: send Twist messages on the /turtle1/cmd_vel topic.
    # Arguments are (message type, topic name, queue size).
    pub = node.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    try:
        # Set your linear speed and distance
        linear_speed = 0.2  # In meters per sec
        distance = 1.0      # In meters

        # Call the move turtle function made above
        move_turtle(linear_speed, distance)

        # Shut down cleanly
        node.destroy_node()
        rclpy.shutdown()
    except KeyboardInterrupt:
        pass
    finally:
        # Shut down cleanly
        node.destroy_node()
        rclpy.shutdown()