from TaskComponent import TaskComponent
from Leaf import Leaf


class Project(object):

    def __init__(self):
        self.task_list = []
        self.engr_list = []

    def initialize(self):
        for task in self.task_list:
            task.initialize(self)

    def add_task(self, task):
        self.task_list.append(task)

    def add_engineer(self, engr):
        self.engr_list.append(engr)

    def get_task(self, taskid):
        for task in self.task_list:
            if task.id == taskid:
                return task
        print "no task of that id is found in the task list"
        return None

    def get_engineer(self, engrid):
        for engr in self.engr_list:
            if engr.id == engrid:
                return engr
        print "no engineer of that id is found in the engineer list"
        return None


    def get_estimated_total_hours(self, taskid):
        task = self.get_task(taskid)
        return task.get_remaining_hours()

    def get_percent_complete(self, taskid):
        task = self.get_task(taskid)
        return task.get_percent_completion()

    def get_estimated_remaining_hours(self, taskid):
        task = self.get_task(taskid)
        return task.get_remaining_hours

    def get_estimated_work_days(self, taskid):
        task = self.get_task(taskid)
        return task.get_work_days_left()
