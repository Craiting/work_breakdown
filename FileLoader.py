import json
from Leaf import Leaf
from Sequential import Sequential
from Parallel import Parallel
from TaskList import TaskList

class FileLoader(object):

    @staticmethod
    def read_from_json(filename): # make tasks and return the list
        task_list = TaskList()
        with open('houseproject.json') as data_file:
            data = json.load(data_file)
        for task in data['Leafs']:
            leaf_task = Leaf(task['id'],task['label'],task['description'],
                             task['original_hours'],task['revised_hours'],
                             task['percent_complete'],task['est_remaining_hrs'],
                             task['est_remaining_workdays'])
            task_list.add(leaf_task)
        for task in data['Sequential']:
            seq_task = Sequential(task['id'],task['label'],task['description'],
                                  task['children'])
            task_list.add(seq_task)
        return task_list.task_list
