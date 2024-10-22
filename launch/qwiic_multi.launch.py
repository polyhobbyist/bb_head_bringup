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
                {'frame_ids': ['left_depth_link', 'front_depth_link', 'right_depth_link'] },
                {'frame_id': 'depth_link'},
                {'multiplexer_address':  112 },
                {'multiplexer_ports': [1, 0, 7] },
            ]),
    ])
