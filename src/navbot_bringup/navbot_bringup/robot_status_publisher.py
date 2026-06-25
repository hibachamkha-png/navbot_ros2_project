import rclpy
from rclpy.node import Node
from navbot_interfaces.msg import RobotStatus


class RobotStatusPublisher(Node):
    def __init__(self):
        super().__init__('robot_status_publisher')

        self.declare_parameter('robot_name', 'NavBot')
        self.declare_parameter('battery_level', 85.0)
        self.declare_parameter('status', 'moving')

        self.publisher_ = self.create_publisher(RobotStatus, 'robot_status', 10)
        self.timer = self.create_timer(1.0, self.publish_status)

    def publish_status(self):
        msg = RobotStatus()

        msg.robot_name = self.get_parameter('robot_name').value
        msg.battery_level = self.get_parameter('battery_level').value
        msg.status = self.get_parameter('status').value

        self.publisher_.publish(msg)
        self.get_logger().info(
            f'Publishing: robot_name={msg.robot_name}, battery={msg.battery_level}, status={msg.status}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = RobotStatusPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
