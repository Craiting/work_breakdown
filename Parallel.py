from TaskComponent import TaskComponent

class Parallel(TaskComponent):

    def __init__(self, id, lable,description, original_hours, revised_hours, percent_complete, est_remaining_hrs, est_remaining_workdays, subtasks = []):
        super(Parallel, self).__init__(id, lable,description, original_hours, revised_hours, percent_complete, est_remaining_hrs, est_remaining_workdays)
        self.subtask_ids = subtasks
        self.subtasks = []

    def load_subtasks(self, tasklist):
        for t in subtask_ids:
            self.subtasks.append(tasklist.get_task(t))
