from TaskComponent import TaskComponent


class TaskList(object):

    def __init__(self):
        self.task_list = []

    def get_task(self, taskid):
        for task in self.task_list:
            if task.id == taskid:
                return task
        print "no task of that id is found in the task list"
        return None

    def add(self, task):
        self.task_list.append(task)
