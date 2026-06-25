import rclpy
from rclpy.node import Node
from navbot_interfaces.srv import GetRobotStatus


class RobotStatusServer(Node):
    def __init__(self):
        super().__init__('robot_status_server')
        self.service = self.create_service(
            GetRobotStatus,
            'get_robot_status',
            self.get_status_callback
        )
        self.get_logger().info('Robot Status Server is ready.')

    def get_status_callback(self, request, response):
        if request.request_status:
            response.robot_name = 'NavBot'
            response.battery_level = 85.0
            response.status = 'moving'
        else:
            response.robot_name = 'Unknown'
            response.battery_level = 0.0
            response.status = 'no request'

        self.get_logger().info('Robot status requested.')
        return response


def main(args=None):
    rclpy.init(args=args)
    node = RobotStatusServer()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
