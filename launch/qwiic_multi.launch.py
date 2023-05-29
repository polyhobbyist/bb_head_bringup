from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='ros_qwiic_tof',
            executable='ros_qwiic_tof',
            name='ros_qwiic_tof',
            output='screen',
            parameters=[
                {'frame_ids': ['depth1', 'depth2', 'depth3'] },
                {'multiplexer_address':  112 },
                {'multiplexer_ports': [1, 8, 7] },
            ]),
    ])