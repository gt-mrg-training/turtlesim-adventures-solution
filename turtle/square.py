import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Square(Node):

    def __init__(self):
        super().__init__('turtle_square')

        self.cmd_pub = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

        self.count = 0
        self.dir = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        self.currDirection = 0
    
        self.timer = self.create_timer(0.5, self.callback)
    
    def callback(self):
        if self.count > 3:
            self.currDirection = (self.currDirection + 1) % len(self.dir)
            self.count = 0
        self.count += 1
        
        xy = self.dir[self.currDirection]

        msg = Twist()
        msg.linear.x = float(xy[0])
        msg.linear.y = float(xy[1])

        self.get_logger().info(f'Publishing {xy}')
        self.cmd_pub.publish(msg)
        


def main(args=None):

    rclpy.init(args=args)

    node = Square()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()