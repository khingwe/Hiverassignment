import unittest
from unittest.mock import patch
from unittest.mock import MagicMock
from unittest.mock import Mock
from robot import Robot
from finder import Finder

class TestRobot(unittest.TestCase):
    """
    Class to test Robot class
    """
    def test_action_1(self):
        """
        Basic Moves
        """
        self.instance = Robot()
        instructions = ['M','L','R','?','Q']
        for x in instructions:
            self.instance.action(x)
        assert self.instance.x == 0
        assert self.instance.y == 1
        assert self.instance.face == 0
        assert self.instance.exit == True

    def test_action_2(self):
        """
        Multiple Direction and Move
        """
        self.instance = Robot()
        instructions = ['R','M','M','R','L']
        for x in instructions:
            self.instance.action(x)
        assert self.instance.x == 2
        assert self.instance.y == 0
        assert self.instance.face == 3

    def test_action_invalid(self):
        """
        Invalid Move
        """
        self.instance = Robot()
        instructions = ['r']
        for x in instructions:
            self.instance.action(x)
        assert self.instance.x == 0
        assert self.instance.y == 0
        assert self.instance.face == 0
        assert self.instance.exit == False

    @patch('robot.Robot.get_input', return_value='Q')
    def test_run_robot_exit(self, mock):
        self.instance = Robot()
        self.instance.runRobot()
        assert self.instance.exit == True


class TestFinder(unittest.TestCase):
    """
    Class to test Finder class
    """
    def test_finder_multiple(self):
        finder = Finder([None,"dsa",None,"sad"])
        assert finder.find("sad") == ["dsa","sad"]

    def test_finder_invalid(self):
        try:
            finder = Finder({})
        except ValueError as ve:
            assert True
        except Exception as ex:
            assert False

    def test_finder_single(self):
        finder = Finder([None,"dsad",None,"rweew","rtdfj"])
        assert finder.find("ftdjr") == "rtdfj"

    def test_finder_empty(self):
        finder = Finder([])
        assert finder.find("ftdjr") == None

if __name__ == '__main__':
    unittest.main()
