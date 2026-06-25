from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='navbot_bringup',
            executable='robot_status_publisher',
            name='robot_status_publisher'
        ),
        Node(
            package='navbot_bringup',
            executable='robot_status_subscriber',
            name='robot_status_subscriber'
        ),
    ])
