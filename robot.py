DIR = ['North','West','South','East']
CMD = ['L', 'M', 'R', 'Q','?']
class Robot:
    def __init__(self):
        """
        x: for x-axis cordinate
        y: for y-axis cordinate
        face: for the direction (For North, South, East, West)
        exit: Flag to intruct shut down
        """
        self.x = 0
        self.y = 0
        self.face = 0
        self.exit = False

    def get_input(self):
        """
        Get in put and return
        """
        return str(input(">"))

    def action(self, command):
        """
        Perform Action as per the Command
        If valid command then perform the operation else
        be in same state and print invalid command
        """
        try:
            if command == 'L':
                self.face = (self.face + 1)%4
            if command == 'R':
                self.face = (self.face - 1)%4
            if command == 'M':
                if self.face == 0:
                    self.y += 1
                if self.face == 2:
                    self.y -= 1
                if self.face == 3:
                    self.x += 1
                if self.face == 1:
                    self.x -= 1
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
        except Exception as ex:
            print("ERROR: System Failure While Executing Command")
            print("ERROR MSG: {}".format(str(ex)))
            raise ex


    def status(self):
        """
        Current Status of Robot
        """
        print("Robot at ({0}, {1}) facing {2}".format(self.x, self.y, DIR[self.face]))

    @staticmethod
    def online():
        """
        To print online message on screen
        """
        print("Hello! Robot coming online.\n",
              "Command the robot with:\n",
              "L - turn left\n",
              "R - turn right\n",
              "M - move forward\n",
              "? - print this message\n",
              "Q - quit\n")

    def runRobot(self):
        """
        Run the Robot as per the Command
        this fuction will be run in infinite loop
        till it gets the shutdown command
        """
        try:
            self.online()
            while(self.exit is False):
                self.action(self.get_input())
                if self.exit == False:
                    self.status()
        except Exception as ex:
            print("ERROR: Run Robot Failed: {}".format(str))
            raise ex

def main():
    """
    Entry Point of the code
    """
    obj = Robot()
    obj.runRobot()

if __name__=="__main__":
    main()
