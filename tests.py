import unittest
from FileLoader import FileLoader
from Project import Project
from Leaf import Leaf
from Parallel import Parallel
from Sequential import Sequential
from Engineer import Engineer


class TestFileLoader(unittest.TestCase):

    def setUp(self):
        self.json_file = "houseproject.json"

    def test_read_from_json(self):
        self.project = FileLoader.read_from_json(self.json_file)
        self.assertTrue(type(self.project) == Project) # should return a Project
        self.assertEqual(len(self.project.task_list),22) # This file has 22 tasks
        self.assertEqual(len(self.project.engr_list), 6) # and 6 engineers

class TestLeafConstruction(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.project = FileLoader.read_from_json('houseproject.json')

    def test_Leaf_task_creation(self):
        task_id = 55
        label = "Landscaping"
        description = "Plant trees, grass, and place rocks"
        original_hours = 12
        revised_hours = 14
        percent_complete = 25
        est_remaining_hrs = 8
        est_remaining_workdays = 1
        engineers = [1,2,3]
        leaf = Leaf(task_id, label, description, original_hours, revised_hours,
                    percent_complete, est_remaining_hrs, est_remaining_workdays,
                    engineers)
        self.assertTrue(type(leaf) == Leaf)
        self.assertTrue(leaf.id == 55)
        self.assertEqual(leaf.percent_complete,25)
        self.assertTrue(leaf.engineers == [1,2,3])

    def test_initialize_gets_engineers(self):
        leaf_task = self.project.get_task(3)
        self.assertEqual(3, len(leaf_task.engineers))
        e1 = self.project.get_engineer(1)
        e2 = self.project.get_engineer(2)
        e3 = self.project.get_engineer(3)
        self.assertEqual([e1,e2,e3], leaf_task.engineers)

class TestParallelTask(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.project = FileLoader.read_from_json('houseproject.json')

    def test_parallel_task_creation(self):
        pid = 25
        label = "parallel task"
        description = "description"
        children = [1,2,3]
        parallel_task = Parallel(pid, label, description, children)
        self.assertTrue(type(parallel_task), Parallel)
        self.assertTrue(parallel_task.id == 25)
        self.assertTrue(parallel_task.label == "parallel task")

    def test_initialize_gets_subtasks(self):
        parallel_task = self.project.get_task(17)
        self.assertEqual(4, len(parallel_task.subtasks))
        t1 = self.project.get_task(9)
        t2 = self.project.get_task(10)
        t3 = self.project.get_task(11)
        t4 = self.project.get_task(12)
        self.assertEqual([t1,t2,t3,t4], parallel_task.subtasks)


class TestSequentialTask(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.project = FileLoader.read_from_json('houseproject.json')

    def test_parallel_task_creation(self):
        pid = 21
        label = "sequential task"
        description = "description"
        children = [1,3]
        sequential_task = Sequential(pid, label, description, children)
        self.assertTrue(type(sequential_task), Sequential)
        self.assertTrue(sequential_task.id == 21)
        self.assertTrue(sequential_task.label == "sequential task")

    def test_initialize_gets_subtasks(self):
        parallel_task = self.project.get_task(19)
        self.assertEqual(3, len(parallel_task.subtasks))
        t1 = self.project.get_task(1)
        t2 = self.project.get_task(2)
        t3 = self.project.get_task(3)
        self.assertEqual([t1,t2,t3], parallel_task.subtasks)


class TestProject(unittest.TestCase):

    def setUp(self):
        unittest.TestCase.setUp(self)
        self.project = FileLoader.read_from_json('houseproject.json')

    def test_get_task(self):
        sample_task = self.project.get_task(7)
        self.assertEqual(sample_task.id, 7)
        self.assertTrue(sample_task.label == "Plumbing")

    def test_get_engineer(self):
        engineer = self.project.get_engineer(4)
        self.assertEqual(engineer.id, 4)
        self.assertTrue(engineer.name == "Agro")
        self.assertEqual(engineer.available_hours, 5)

    def test_add_task(self):
        task = Parallel(1,"Label","description",[4,2,3])
        project = Project()
        project.add_task(task)
        self.assertEqual(len(project.task_list), 1)
        self.assertEqual(project.get_task(1), task)

    def test_add_engineer(self):
        engineer = Engineer(88,"Jameses",5)
        project = Project()
        project.add_engineer(engineer)
        self.assertEqual(len(project.engr_list), 1)
        self.assertEqual(project.get_engineer(88), engineer)

    def test_get_estimated_work_days_leaf(self):
        days = self.project.get_estimated_work_days(4)
        self.assertEqual(2,days)

    def test_get_estimated_work_days_sequential_parent(self):
        days_to_completion = self.project.get_estimated_work_days(22) # Sequential Task Basement
        self.assertEqual(9,days_to_completion)

    def test_get_estimated_work_days_parallel_parent(self):
        days_to_completion = self.project.get_estimated_work_days(17) # Parallel Task Basement
        self.assertEqual(2,days_to_completion)

    def test_get_percent_complete_sequential_parent(self):
        percent_left = self.project.get_percent_complete(21)
        self.assertEqual(50.0, percent_left)

    def test_get_percent_complete_parallel_parent(self):
        percent_left = self.project.get_percent_complete(16)
        self.assertEqual(12.78, percent_left)

    def test_get_total_hours_leaf(self):
        total_hours = self.project.get_estimated_total_hours(5)
        self.assertEqual(21,total_hours)

    def test_get_total_hours_sequential_parent(self):
        total_hours = self.project.get_estimated_total_hours(19)
        self.assertEqual(11, total_hours)

    def test_get_total_hours_parallel_parent(self):
        total_hours = self.project.get_estimated_total_hours(18)
        self.assertEqual(135,total_hours)




if __name__ == '__main__':
    unittest.main()
