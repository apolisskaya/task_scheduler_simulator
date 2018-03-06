# Model file for Task objects used in simulation
# task number, cpu_demand, power_demand, and priority are user-defined
# Priority: 1 to 5, with 1 being lowest, 5 being highest. Priority 0 may be assigned to tasks that will never run.
# Status: 0 if waiting, 1 if currently being executed, 2 if completed

import datetime


class Task:

    def __init__(self, cpu_demand, power_demand, priority, deadline, execution_time, id, processor=None):
        self.cpu_demand = cpu_demand
        self.power_demand = power_demand
        self.priority = priority
        self.status = 0
        self.deadline = deadline
        self.id = id
        self.execution_time = execution_time
        self.on_processor = processor
        self.hit_deadline = None
        self.origination_time = datetime.datetime.now()  # record the time when the task is created
        self.start_time = None

    # allows pushing objects with non-unique priority into priority queue
    def __lt__(self, other):
        return ((self.cpu_demand, self.power_demand, self.priority, self.status, self.deadline,
                 self.id, self.on_processor, self.hit_deadline, self.execution_time, self.origination_time,
                 self.start_time) < (other.cpu_demand, other.power_demand, other.priority, other.status, other.deadline,
                                     other.id, other.on_processor, other.hit_deadline, other.execution_time,
                                     other.origination_time, other.start_time))

    def change_priority(self, new_priority):
        self.priority = new_priority

    def get_priority(self):
        return self.priority

    def change_status(self):
        self.status += 1

    def remove_from_queue(self):
        self.priority = 0

    def begin_task(self):
        self.change_status()
        self.start_time = datetime.datetime.now()

    def set_processor(self, processor):
        self.on_processor = processor

    def get_processor(self):
        return self.on_processor

    def complete_task(self):
        if datetime.datetime.now() <= self.deadline:
            self.hit_deadline = 1
        else:
            self.hit_deadline = 0
        self.change_status()

    def __repr__(self):
        for attribute, value in self.__dict__.items():
            if value is not None:
                print(attribute, str(value))

    def __del__(self):
        if self.status != 2:
            print('Task ', self.id, ' destroyed but never ran. Status', self.status)