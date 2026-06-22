import rclpy
from rclpy.node import Node
from std_msgs.msg import String


class HelloNavBotPublisher(Node):
    def __init__(self):
        super().__init__('hello_navbot_publisher')
        self.publisher_ = self.create_publisher(String, 'hello_navbot', 10)
        self.timer = self.create_timer(1.0, self.publish_message)
        self.counter = 0

    def publish_message(self):
        msg = String()
        msg.data = f'Hello NavBot: {self.counter}'
        self.publisher_.publish(msg)
        self.get_logger().info(f'Publishing: "{msg.data}"')
        self.counter += 1


def main(args=None):
    rclpy.init(args=args)
    node = HelloNavBotPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
