
from robot import Robot

class Fleet:
    def __init__(self, robot, robot1, robot2):
        self.name = "The Fleet"
        self.robot = robot
        self.robot1 = robot1
        self.robot2 = robot2
        self.robot_dict = {
            self.robot.name: self.robot.health,
            self.robot1.name: self.robot1.health,
            self.robot2.name: self.robot2.health
        }

        self.robot_list_names = [self.robot.name, self.robot1.name, self.robot2.name]
        self.robot_list = [self.robot, self.robot1, self.robot2]
       
