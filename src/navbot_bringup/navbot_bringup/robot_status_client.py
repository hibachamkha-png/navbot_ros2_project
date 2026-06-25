import rclpy
from rclpy.node import Node
from navbot_interfaces.srv import GetRobotStatus


class RobotStatusClient(Node):
    def __init__(self):
        super().__init__('robot_status_client')
        self.client = self.create_client(GetRobotStatus, 'get_robot_status')

        while not self.client.wait_for_service(timeout_sec=1.0):
            self.get_logger().info('Waiting for service...')

    def send_request(self):
        request = GetRobotStatus.Request()
        request.request_status = True

        future = self.client.call_async(request)
        rclpy.spin_until_future_complete(self, future)

        response = future.result()
        self.get_logger().info(
            f'Received status: robot_name={response.robot_name}, '
            f'battery={response.battery_level}, status={response.status}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = RobotStatusClient()
    node.send_request()
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
