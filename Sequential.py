from TaskComponent import TaskComponent

class Sequential(TaskComponent):

    def __init__(self, id, label, description, subtasks = []):
        super(Sequential, self).__init__(id, label,description, original_hours=None,
                                         revised_hours=None, percent_complete=None,
                                         est_remaining_hrs=None, est_remaining_workdays=None)
        self.subtask_ids = subtasks
        self.subtasks = []

    def initialize(self, project):
        for t in self.subtask_ids:
            self.subtasks.append(project.get_task(t))

    def __repr__(self):
        return "seq: %d | %s" % (self.id, self.label)

    def get_work_days_left(self):
        total_workdays = 0
        for task in self.subtasks:
            total_workdays = total_workdays + task.get_work_days_left()
        return total_workdays

    def get_remaining_hours(self):
        total_hours = 0
        for task in self.subtasks:
            total_hours = total_hours + task.get_remaining_hours()
        return total_hours

    def get_percent_completion(self):
        task_length = len(self.subtasks)
        total_percent = 0
        for task in self.subtasks:
            total_percent = total_percent + task.get_percent_completion()
        percent = float(total_percent)/float(task_length)
        return round(percent, 2)
