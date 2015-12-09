from TaskComponent import TaskComponent

class Leaf(TaskComponent):

    def __init__(self, id, label,description, original_hours, revised_hours,
                 percent_complete, est_remaining_hrs, est_remaining_workdays,
                 engineers):
        super(Leaf, self).__init__(id, label,description, original_hours,
                                   revised_hours, percent_complete,
                                   est_remaining_hrs, est_remaining_workdays)
        self.engineers = engineers

    def __repr__(self):
        return "task: %d | %s" % (self.id, self.label)

    def initialize(self, project):
        engrs = self.engineers
        self.engineers = []
        for e in engrs:
            engineer = project.get_engineer(e)
            self.engineers.append(engineer)

    def get_work_days_left(self):
        if(len(self.engineers) == 0):
            return 99
        return int(self.est_remaining_workdays)

    def get_remaining_hours(self):
        return int(self.est_remaining_hrs)

    def get_percent_completion(self):
        return float(self.percent_complete)
