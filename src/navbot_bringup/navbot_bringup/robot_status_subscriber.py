import rclpy
from rclpy.node import Node
from navbot_interfaces.msg import RobotStatus


class RobotStatusSubscriber(Node):
    def __init__(self):
        super().__init__('robot_status_subscriber')
        self.subscription = self.create_subscription(
            RobotStatus,
            'robot_status',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(
            f'I received: robot_name={msg.robot_name}, battery={msg.battery_level}, status={msg.status}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = RobotStatusSubscriber()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
