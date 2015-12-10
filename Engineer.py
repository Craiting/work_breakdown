


class Engineer(object):

    def __init__(self, id, name, available_hours):
        self.id = id
        self.name = name
        self.available_hours = available_hours

    def __repr__(self):
        return "Engineer: %s works %d hours" % (self.name, self.available_hours)

    def get_tasks(self,project):
        tasks = []
        for task in project.task_list:
            for e in task.engineers:
                if self.id == e.id and task.id not in tasks:
                    tasks.append(task.id)
        return tasks
