from TaskComponent import TaskComponent

class Sequential(TaskComponent):

    def __init__(self, id, label,description, subtasks = []):
        super(Sequential, self).__init__(id, label,description, original_hours=None,
                                         revised_hours=None, percent_complete=None,
                                         est_remaining_hrs=None, est_remaining_workdays=None)
        self.original_hours
        self.revised_hours
        self.percent_complete
        self.est_remaining_hrs
        self.est_remaining_workdays
        self.subtask_ids = subtasks
        self.subtasks = []

    def load_subtasks(self, tasklist):
        for t in subtask_ids:
            self.subtasks.append(tasklist.get_task(t))

    def __repr__(self):
        return "seq: %d | %s" % (self.id, self.label)
