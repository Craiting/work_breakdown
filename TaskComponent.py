

class TaskComponent(object):

    def __init__(self, id, label, description, original_hours, revised_hours, percent_complete, est_remaining_hrs, est_remaining_workdays):
        self.id = id
        self.label = label
        self.description = description
        self.original_hours = original_hours
        self.revised_hours = revised_hours
        self.percent_complete = percent_complete
        self.est_remaining_hrs = est_remaining_hrs
        self.est_remaining_workdays = est_remaining_workdays
        self.engineers = []
