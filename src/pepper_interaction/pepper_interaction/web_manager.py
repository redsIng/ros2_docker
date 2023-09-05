import rclpy

from rclpy.node import Node
from std_msgs.msg import Int32


class WebManager(Node):
        def __init__(self):
                super().__init__('web_manager')
                self.web_subscriber = self.create_subscription(Int32, 'web_commands', self.web_callback, 10)
                self.web_subscriber  # prevent unused variable warning
        def web_callback(self, msg):
                self.get_logger().info('Received: "%d"' % msg.data)
def main():
        rclpy.init()
        node = WebManager()
        rclpy.spin(node)
        rclpy.shutdown()

if __name__ == '__main__':
        main()
