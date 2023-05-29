import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.substitutions import LaunchConfiguration, PythonLaunchDescriptionSource
from launch_ros.actions import Node

def generate_launch_description():

    urdf_file_name = 'bb_head.urdf'
    urdf = os.path.join(
        get_package_share_directory('bb_description'),
        urdf_file_name)
    with open(urdf, 'r') as infp:
        robot_desc = infp.read()

    return LaunchDescription([
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            output='screen',
            parameters=[{'use_sim_time': 'false', 'robot_description': robot_desc}],
            arguments=[urdf]),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [os.path.join(get_package_share_directory('bb_head_bringup'), 'launch', 'qwiic_multi.launch.py')]
            )
        )
    ])