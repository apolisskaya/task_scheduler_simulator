# Model file for Processor and Battery objects used in simulation
# status: 0 when unused, 1 when busy
# power_available: the amount of power available at time of initialization
# power_max: the maximum possible amount of electrical charge

import itertools


class Battery:
    def __init__(self, power_available, power_max):
        self.power_max = power_max
        self.power_available = power_available
        self.power_minimum = 5   # TODO: may need to change this to be dynamically set on init


class Processor:
    new_id = itertools.count().__next__()

    def __init__(self, power_available, power_max):
        self.status = 0
        self.id = Processor.new_id
        self.battery = Battery(power_available, power_max)
        self.currently_executing_task = None

    def run_task(self, task):
        if task.power_demand < self.battery.power_available and \
                                self.battery.power_available - task.power_demand > self.battery.power_minimum:
            print('Task', str(task.id), 'now running on Processor', self.id)
            self.battery.power_available -= task.power_demand

    def set_current_task(self, task):
        self.currently_executing_task = task.id
        self.status = 1