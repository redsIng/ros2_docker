import launch
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.conditions import IfCondition
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        # Declare a launch argument for the port number (adjust as needed)
        DeclareLaunchArgument(
            'websocket_port',
            default_value='9090',
            description='WebSocket server port'
        ),

        # Start the rosbridge_websocket server
        Node(
            package='rosbridge_server',
            executable='rosbridge_websocket',
            name='rosbridge_server',
            namespace='',
            output='screen',
            parameters=[{'address': '192.168.122.1'}],  # Add any additional parameters if needed
            #arguments=[['url_path:=/workspaces/ros2_docker/src/pepper_interaction/scripts/web_interface/index.html']],  # Add parameter file path if needed
            #remappings=[('/web_commands', '/web_commands')]  # Remap topics if needed
        ),
    ])
