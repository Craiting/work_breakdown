import unittest
from FileLoader import FileLoader
from TaskList import TaskList


class TestTreeSetup(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.task_list = FileLoader.read_from_json('houseproject.json')

    def test_thing(self):
        for t in self.task_list:
            print t
        self.assertTrue(self.task_list>0)


if __name__ == '__main__':
    unittest.main()
