import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from std_msgs.msg import Int8

class CountSquares(Node):

    def __init__(self):
        super().__init__('count_squares')

        self.squares = 0    

        self.firstPos = (0, 0)
        self.currPos = [0, 0]

        self.vel_sub = self.create_subscription(Twist, '/turtle1/cmd_vel', self.callback, 10)

        self.count_pub = self.create_publisher(Int8, 'square_count', 10)
    
    def callback(self, vel:Twist):
        self.currPos[0] += vel.linear.x
        self.currPos[1] += vel.linear.y

        if self.firstPos[0] == self.currPos[0] and self.firstPos[1] == self.currPos[1]:
            self.squares += 1 
        
        msg = Int8()
        msg.data = self.squares
        self.count_pub.publish(msg)


def main(args=None):

    rclpy.init(args=args)

    node = CountSquares()

    rclpy.spin(node)

    node.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()