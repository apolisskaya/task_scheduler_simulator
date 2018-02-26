# Model file for Processor and Battery objects used in simulation
# status: 0 when unused, 1 when busy
# power_available: the amount of power available at time of initialization
# power_max: the maximum possible amount of electrical charge


class Battery:
    def __init__(self, power_available, power_max):
        self.power_max = power_max
        self.power_available = power_available
        self.power_minimum = 5

    def charge_capacitor(self, charge_amount):
        if self.power_available + charge_amount <= self.power_max:
            self.power_available += charge_amount
        else:
            self.power_available = self.power_max


class Processor:

    def __init__(self, power_available, power_max, id=0):
        self.status = 0
        self.id = id
        self.battery = Battery(power_available, power_max)
        self.currently_executing_task = None

    def run_task(self, task):
        self.battery.power_available -= task.power_demand
        self.complete_task()

    def set_current_task(self, task):
        self.currently_executing_task = task.id
        self.status = 1

    def complete_task(self):
        self.status = 0
        self.currently_executing_task = None


class SuperCapacitor:  # the supercap and microprocessor are one object for our purposes here
    def __init__(self, power_available, power_max):
        self.battery = Battery(power_available, power_max)
        self.current_processor = None
        self.all_processors = []

    def switch_processor(self, new_processor):
        if new_processor in self.all_processors:
            self.current_processor = new_processor
        else:
            print('Something went wrong. Requested processor does not exist.')

    def lose_power(self, power_deduction):
        if self.battery.power_available - power_deduction > self.battery.power_minimum:
            self.battery.power_available -= power_deduction
        else:
            print('Not enough power available to keep running Peripheral ', str(self.current_processor))

    def add_power(self, power_addition):
        if self.battery.power_available + power_addition <= self.battery.power_max:
            self.battery.power_available += power_addition
        else:
            self.battery.power_available = self.battery.power_max

    def add_new_processor(self, processor):
        self.all_processors.append(processor)