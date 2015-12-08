from TaskComponent import TaskComponent

class Leaf(TaskComponent):

    def __init__(self, id, label,description, original_hours, revised_hours,
                 percent_complete, est_remaining_hrs, est_remaining_workdays):
        super(Leaf, self).__init__(id, label,description, original_hours,
                                   revised_hours, percent_complete,
                                   est_remaining_hrs, est_remaining_workdays)
        self.engineers = []

    def __repr__(self):
        return "task: %d | %s" % (self.id, self.label)
