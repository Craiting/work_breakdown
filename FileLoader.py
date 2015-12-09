import json
from Leaf import Leaf
from Sequential import Sequential
from Parallel import Parallel
from Project import Project
from Engineer import Engineer

class FileLoader(object):

    @staticmethod
    def read_from_json(filename): # make tasks and return the list
        task_list = Project()
        with open('houseproject.json') as data_file:
            data = json.load(data_file)
        for task in data['Leafs']:
            leaf_task = Leaf(task['id'],task['label'],task['description'],
                             task['original_hours'],task['revised_hours'],
                             task['percent_complete'],task['est_remaining_hrs'],
                             int(task['est_remaining_workdays']), task['engineers'])
            task_list.add_task(leaf_task)
        for task in data['Sequential']:
            seq_task = Sequential(task['id'],task['label'],task['description'],
                                  task['children'])
            task_list.add_task(seq_task)
        for task in data['Parallel']:
            par_task = Parallel(task['id'], task['label'],task['description'],
                                task['children'])
            task_list.add_task(par_task)
        for engr in data['engineers']:
            engineer = Engineer(engr['id'], engr['name'], engr['available_hours'])
            task_list.add_engineer(engineer)
        task_list.initialize()
        return task_list
