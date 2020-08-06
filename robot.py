DIR = ['North','West','South','East']
CMD = ['L', 'M', 'R', 'Q','?']
class Robot:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.face = 0
        self.exit = False

    def get_input(self):
        return str(input(">"))

    def action(self, command):
        if command == 'L':
            self.face = (self.face + 1)%4
        if command == 'R':
            self.face = (self.face - 1)%4
        if command == 'M':
            if self.face == 0:
                self.x += 1
            if self.face == 2:
                self.x -= 1
            if self.face == 3:
                self.y += 1
            if self.face == 1:
                self.y -= 1
        if command == 'Q':
            self.exit = True
            print("Robot shutting down.\n")
        if command == '?':
            print("Command the robot with:\n",
                  "L - turn left\n",
                  "R - turn right\n",
                  "M - move forward\n",
                  "? - print this message\n",
                  "Q - quit\n")
        if command not in CMD:
            print("invalid command")

    def status(self):
        print("Robot at ({0}, {1}) facing {2}".format(self.x, self.y, DIR[self.face]))

    @staticmethod
    def online():
        print("Hello! Robot coming online.\n",
              "Command the robot with:\n",
              "L - turn left\n",
              "R - turn right\n",
              "M - move forward\n",
              "? - print this message\n",
              "Q - quit\n")

    def runRobot(self):
        self.online()
        while(self.exit is False):
            self.action(self.get_input())
            if self.exit == False:
                self.status()

obj = Robot()
obj.runRobot()
