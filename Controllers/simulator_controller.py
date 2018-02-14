from multiprocessing import Process  # https://stackoverflow.com/questions/3474382/how-do-i-run-two-python-loops-concurrently
import queue, time, operator

from Controllers import task_controller as tc
from Services import performance_service as ps

# Main Controller for Simulations
# Contains different scheduling approaches
# May also end up containing performance evaluation metrics - should probably be in a different file

# For now, these will just run the simulation with all tasks sent to scheduler at the same time.


def process_tasks_in_queue(processor, task_queue):
    completed_tasks, failed_tasks = [], []

    while not task_queue.empty():
        current_task = task_queue.get()
        # check that processor has enough juice to execute the task
        if (current_task.power_demand < processor.battery.power_available) and processor.battery.power_available - current_task.power_demand > processor.battery.power_minimum:
            tc.assign_task_to_processor(task=current_task, processor=processor)
            time.sleep(current_task.execution_time)  # seconds
            processor.run_task(task=current_task)
            current_task.complete_task()
            completed_tasks.append(current_task)
        else:
            failed_tasks.append(current_task)

    return completed_tasks, failed_tasks


def run_fifo_simulation(processor):
    task_queue = queue.Queue()
    tc.generate_tasks(task_queue)
    completed_tasks, failed_tasks = process_tasks_in_queue(processor, task_queue)

    ps.run_performance_evaluation()

    task_queue.queue.clear()
    return 0


def run_priority_simulation(processor):
    task_queue = queue.PriorityQueue()
    tc.generate_task_and_task_property_tuples(task_queue, 'priority')
    completed_tasks, failed_tasks = process_tasks_in_queue(processor, task_queue)

    ps.run_performance_evaluation()

    task_queue.queue.clear()
    return 0


def run_earliest_deadline_simulation(processor):
    task_queue = queue.PriorityQueue()
    tc.generate_task_and_task_property_tuples(task_queue, 'deadline')
    completed_tasks, failed_tasks = process_tasks_in_queue(processor, task_queue)

    ps.run_performance_evaluation()

    task_queue.queue.clear()

    return 0


# Simulations taking some random number of tasks without priority shifting!!!
def run_algorithm_1_simulation(processor, number_of_tasks):
    # Version 1: Earliest Deadline First, with priority as the first tiebreaker and exec time as the second
    task_queue = queue.Queue()
    task_list = []
    # TODO: list comprehension possible here?
    for i in range(0, number_of_tasks):
        task_list.append(tc.generate_new_task())
    task_list.sort(key=operator.attrgetter('deadline', 'priority', 'execution_time'))
    for i in range(0, number_of_tasks):
        task_queue.put(task_list[i])
    completed_tasks, failed_tasks = process_tasks_in_queue(processor, task_queue)

    ps.run_performance_evaluation()

    task_queue.queue.clear()

    return 0


def run_algorithm_2_simulation(number_of_tasks):
    # Version 2: Earliest Deadline First, with exec time as first tiebreaker and priority as second
    task_queue = queue.Queue()
    task_list = []
    for i in range(0, number_of_tasks):
        task_list.append(tc.generate_new_task())
    task_list.sort(key=operator.attrgetter('deadline', 'execution_time', 'priority'))

    ps.run_performance_evaluation()

    return 0


def run_algorithm_3_simulation(number_of_tasks):
    # Version 3: Priority first, then earliest deadline, then exec time
    task_queue = queue.Queue()
    task_list = []
    for i in range(0, number_of_tasks):
        task_list.append(tc.generate_new_task())
    task_list.sort(key=operator.attrgetter('priority', 'deadline', 'execution_time'))

    ps.run_performance_evaluation()

    return 0