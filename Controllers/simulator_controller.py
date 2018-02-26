from multiprocessing import Process  # https://stackoverflow.com/questions/3474382/how-do-i-run-two-python-loops-concurrently
import queue, time, operator, random

from Controllers import task_controller as tc
from Services import performance_service as ps
from Models import cpu_model as cm

# Main Controller for Simulations
# Contains different scheduling approaches
# May also end up containing performance evaluation metrics - should probably be in a different file

# For now, these will just run the simulation with all tasks sent to scheduler at the same time.


def process_tasks_in_queue(task_queue, charging=False, charging_scale=1):
    completed_tasks, failed_tasks = [], []

    while not task_queue.empty():
        current_task = task_queue.get()
        # check that processor has enough juice to execute the task
        current_processor = current_task.get_processor()
        if (current_task.power_demand < current_processor.battery.power_available) and current_processor.battery.power_available - \
                current_task.power_demand > current_processor.battery.power_minimum:
            # set processor to run current task and log start time of task for performance purposes
            tc.assign_task_to_processor(task=current_task, processor=current_processor)
            print('running task ', current_task.id, 'on processor', current_processor.id)
            time.sleep(current_task.execution_time)  # seconds
            current_task.get_processor().run_task(current_task)
            # charge the peripheral and supercap if charging is enabled
            if charging:
                current_processor.battery.charge_capacitor(current_task.execution_time * charging_scale)
                current_processor.get_supercap().battery.charge_capacitor(current_task.execution_time *
                                                                                     charging_scale)
            current_task.complete_task()
            completed_tasks.append(current_task)
        else:
            failed_tasks.append(current_task)

    return completed_tasks, failed_tasks


# Simulations taking some random number of tasks without priority shifting!!!
def run_algorithm_1_simulation(number_of_tasks, charging=False, number_of_processors=1, supercap=None):
    # Version 1: Earliest Deadline First, with priority as the first tiebreaker and exec time as the second
    if number_of_processors < 1 or number_of_tasks < 1:
        print('Cannot have tasks with no peripherals or no tasks')
        return -1
    else:
        processor_list = []
        for i in range(number_of_processors):
            # TODO: maybe randomize these values?
            processor_list.append(cm.Processor(id=i, power_available=60, power_max=70))

        task_queue = queue.Queue()

        task_list = [tc.generate_new_task(id=i, processor=random.choice(processor_list)) for i in range(0, number_of_tasks)]
        task_list.sort(key=operator.attrgetter('deadline', 'priority', 'execution_time'))
        for i in range(0, number_of_tasks):
            task_queue.put(task_list[i])
        completed_tasks, failed_tasks = process_tasks_in_queue(task_queue, charging)

        percent_completed, percent_hit_deadline, awt = ps.run_performance_evaluation(completed_tasks, failed_tasks,
                                                                                     "Algorithm 1", number_of_tasks)

        task_queue.queue.clear()

        return percent_completed, percent_hit_deadline, awt


def run_algorithm_2_simulation(number_of_tasks, charging=False, number_of_processors=1, supercap=None):
    # Version 2: Earliest Deadline First, with exec time as first tiebreaker and priority as second

    if number_of_processors < 1 or number_of_tasks < 1:
        print('Cannot have tasks with no peripherals or no tasks')
        return -1
    else:
        processor_list = []
        for i in range(number_of_processors):
            processor_list.append(cm.Processor(id=i, power_available=60, power_max=70))

        task_queue = queue.Queue()
        task_list = [tc.generate_new_task(id=i, processor=random.choice(processor_list)) for i in range(0, number_of_tasks)]
        task_list.sort(key=operator.attrgetter('deadline', 'execution_time', 'priority'))
        for i in range(0, number_of_tasks):
            task_queue.put(task_list[i])
        completed_tasks, failed_tasks = process_tasks_in_queue(task_queue, charging)

        percent_completed, percent_hit_deadline, awt = ps.run_performance_evaluation(completed_tasks, failed_tasks,
                                                                                     "Algorithm 2", number_of_tasks)

        task_queue.queue.clear()

        return percent_completed, percent_hit_deadline, awt


def run_algorithm_3_simulation(number_of_tasks, charging=False, number_of_processors=1, supercap=None):
    # Version 3: Priority first, then earliest deadline, then exec time

    if number_of_processors < 1 or number_of_tasks < 1:
        print('Cannot have tasks with no peripherals or no tasks')
        return -1
    else:
        processor_list = []
        for i in range(number_of_processors):
            processor_list.append(cm.Processor(id=i, power_available=60, power_max=70))

        task_queue = queue.Queue()
        task_list = [tc.generate_new_task(id=i, processor=random.choice(processor_list)) for i in range(0, number_of_tasks)]
        task_list.sort(key=operator.attrgetter('priority', 'deadline', 'execution_time'))
        for i in range(0, number_of_tasks):
            task_queue.put(task_list[i])

        completed_tasks, failed_tasks = process_tasks_in_queue(task_queue, charging)
        percent_completed, percent_hit_deadline, awt = ps.run_performance_evaluation(completed_tasks, failed_tasks,
                                                                                     "Algorithm 3", number_of_tasks)

        task_queue.queue.clear()

        return percent_completed, percent_hit_deadline, awt
