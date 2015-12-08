from TaskComponent import TaskComponent

class Leaf(TaskComponent):

    def __init__(self, id, lable,description, original_hours, revised_hours, percent_complete, est_remaining_hrs, est_remaining_workdays):
        super(Leaf, self).__init__(id, lable,description, original_hours, revised_hours, percent_complete, est_remaining_hrs, est_remaining_workdays)
        self.engineers = [1,2]
        
