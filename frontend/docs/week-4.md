# Week 4: ROS 2 Fundamentals (Continued)

This week, we build upon our understanding of ROS 2 core concepts by exploring more advanced topics essential for developing robust robot applications. We will delve into Quality of Service (QoS) settings, the structure and usage of client libraries, and the critical role of launch files and parameter management in orchestrating complex ROS 2 systems.

## Quality of Service (QoS) Policies

ROS 2's Quality of Service (QoS) settings allow developers to configure the reliability, latency, and longevity of communication between nodes. These policies are crucial for adapting ROS 2 to various application requirements, from high-throughput sensor data to critical control commands.

Key QoS policies include:

-   **History**: Determines how many samples or how much time the middleware should keep.
    -   `KEEP_LAST`: Only the N most recent samples are stored.
    -   `KEEP_ALL`: All samples are stored until resource limits are exhausted.
-   **Depth**: Used with `KEEP_LAST` history to specify the number of samples to keep.
-   **Reliability**: Guarantees about message delivery.
    -   `BEST_EFFORT`: Attempts to deliver messages but may drop them if the network is congested. Suitable for high-frequency, non-critical data (e.g., sensor streams).
    -   `RELIABLE`: Guarantees delivery of every message, potentially with retransmissions. Essential for critical control commands or configuration updates.
-   **Durability**: Concerns whether messages are transient (only available to current subscribers) or persistent (available to future subscribers).
    -   `VOLATILE`: Messages are not retained for new subscribers.
    -   `TRANSIENT_LOCAL`: The last published message is retained and delivered to new subscribers. Useful for configuration data or initial states.
-   **Liveliness**: How the middleware determines if a publisher is still active.
    -   `AUTOMATIC`: Liveliness is asserted automatically by the middleware.
    -   `MANUAL_BY_TOPIC`: Application explicitly asserts liveliness.
-   **Deadline**: The maximum expected time between messages. If a publisher fails to meet this, subscribers are notified.
-   **Lifespan**: The maximum duration for which a message is valid. Messages older than their lifespan are not delivered.

Appropriate QoS settings are vital for ensuring the correct behavior and performance of a distributed robotic system.

## Building ROS 2 Packages with Python

ROS 2 packages are the fundamental unit of organization for ROS 2 code. They contain nodes, launch files, configuration, and other resources. For Python development, `ament_python` is the build tool, and `setup.py` defines the package.

Steps to create and build a Python package:

1.  **Create Package**:
    ```bash
    ros2 pkg create --build-type ament_python my_python_package
    ```
2.  **Define Node Entry Points**: In `setup.py`, specify entry points for your executable Python scripts:
    ```python
    entry_points={
        'console_scripts': [
            'my_node = my_python_package.my_node:main',
        ],
    },
    ```
    Where `my_node` is the name of your executable, `my_python_package` is the Python module (folder), and `my_node` is the Python file containing the `main` function.
3.  **Implement Node Logic**: Write your ROS 2 node logic in Python using `rclpy`.
    ```python
    # my_python_package/my_node.py
    import rclpy
    from rclpy.node import Node
    from std_msgs.msg import String

    class MyPublisher(Node):
        def __init__(self):
            super().__init__('my_publisher')
            self.publisher_ = self.create_publisher(String, 'topic', 10)
            timer_period = 0.5  # seconds
            self.timer = self.create_timer(timer_period, self.timer_callback)
            self.i = 0

        def timer_callback(self):
            msg = String()
            msg.data = 'Hello ROS 2: %d' % self.i
            self.publisher_.publish(msg)
            self.get_logger().info('Publishing: "%s"' % msg.data)
            self.i += 1

    def main(args=None):
        rclpy.init(args=args)
        my_publisher = MyPublisher()
        rclpy.spin(my_publisher)
        my_publisher.destroy_node()
        rclpy.shutdown()

    if __name__ == '__main__':
        main()
    ```
4.  **Build**:
    ```bash
    colcon build --packages-select my_python_package
    ```
5.  **Source and Run**:
    ```bash
    source install/setup.bash
    ros2 run my_python_package my_node
    ```

## Launch Files and Parameter Management

Complex robotic systems often involve many nodes, each with various parameters. **Launch files** provide a convenient way to start and configure multiple ROS 2 nodes simultaneously. They are typically written in Python or XML.

### Python Launch Files
Python launch files offer greater flexibility and programmatic control.

**Example (`my_robot_launch.py`):**
```python
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='my_python_package',
            executable='my_node',
            name='my_publisher_node',
            output='screen',
            parameters=[
                {'publish_frequency': 1.0},
                {'message_prefix': 'Robot says: '}
            ]
        ),
        Node(
            package='another_package',
            executable='another_node',
            name='my_subscriber_node',
            output='log',
        ),
    ])
```
To run: `ros2 launch my_python_package my_robot_launch.py`

### Parameter Management
Parameters allow you to configure the behavior of nodes without recompiling the code.

-   **Declaration**: Parameters are declared within a node (e.g., `self.declare_parameter('my_parameter', 'default_value')`).
-   **Access**: Nodes can get parameter values (`self.get_parameter('my_parameter').value`).
-   **Configuration**:
    -   **Via Launch Files**: As shown above, parameters can be set directly in `Node` declarations.
    -   **Via YAML Files**: Parameters can be loaded from YAML files for more complex configurations:
        ```yaml
        my_publisher_node:
            ros__parameters:
                publish_frequency: 2.0
                message_prefix: "YAML configured: "
        ```
        Then, reference the YAML in the launch file:
        ```python
        from ament_index_python.packages import get_package_share_directory
        import os

        # ...
        Node(
            package='my_python_package',
            executable='my_node',
            name='my_publisher_node',
            output='screen',
            parameters=[os.path.join(
                get_package_share_directory('my_python_package'),
                'config',
                'my_params.yaml'
            )]
        ),
        # ...
        ```
    -   **Dynamically**: Parameters can be set and retrieved at runtime using `ros2 param set` and `ros2 param get` commands.

Understanding launch files and parameter management is crucial for creating scalable and easily configurable ROS 2 robot systems. These tools enable the orchestration of complex behaviors from individual modular components, a cornerstone of successful robotic deployments.
