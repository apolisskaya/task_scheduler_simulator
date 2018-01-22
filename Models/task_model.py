# Model file for Task objects used in simulation
# task number, cpu_demand, power_demand, and priority are user-defined
# Priority: 1 to 5, with 1 being lowest, 5 being highest. Priority 0 may be assigned to tasks that will never run.
# Status: 0 if waiting, 1 if currently being executed, 2 if completed

import itertools, datetime


class Task:
    new_id = itertools.count().__next__()

    def __init__(self, cpu_demand, power_demand, priority, deadline):
        self.cpu_demand = cpu_demand
        self.power_demand = power_demand
        self.priority = priority
        self.status = 0
        self.deadline = deadline
        self.id = Task.new_id
        self.on_processor = None
        self.hit_deadline = None

    def change_priority(self, new_priority):
        self.priority = new_priority

    def change_status(self):
        self.status += 1

    def remove_from_queue(self):
        self.priority = 0

    def set_processor(self, processor):
        self.on_processor = processor.id
        # task is currently running, so update status accordingly
        self.change_status()

    def complete_task(self):
        # check if task was completed on time or not
        if datetime.datetime.now() <= self.deadline:
            self.hit_deadline = 1
        else:
            self.hit_deadline = 0
        self.on_processor = None
        self.change_status()

    def __del__(self):
        print('Task', self.id, 'destroyed. Status', self.status)