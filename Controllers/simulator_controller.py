from multiprocessing import Process  # https://stackoverflow.com/questions/3474382/how-do-i-run-two-python-loops-concurrently
import queue, random, datetime

from Models import task_model, cpu_model
from Controllers import task_controller as tc

# Main Controller for Simulations
# Contains different scheduling approaches
# May also end up containing performance evaluation metrics - should probably be in a different file

# For now, these will just run the simulation with all tasks sent to scheduler at the same time. # TODO: Change this


def run_fifo_simulation(processor):
    task_queue = queue.Queue()
    tc.generate_tasks(task_queue)

    while not task_queue.empty():
        current_task = task_queue.get()
        completed_tasks, failed_tasks = [], []

        # check that processor has enough juice to execute the task
        if current_task.get_power_demand < processor.battery.power_available and processor.battery.power_available - current_task.get_power_demand > processor.battery.power_minimum:
            tc.assign_task_to_processor(task=current_task, processor=processor)
            # TODO: some amount of time for the task to execute
            processor.run_task(task=current_task)
            completed_tasks.append(current_task)
        else:
            failed_tasks.append(current_task)

    # clear any remaining items from the queue
    task_queue.queue.clear()
    return 0


def run_earliest_deadline_simulation():
    task_queue = queue.PriorityQueue()
    # TODO: this needs to return tuples, implementation must be altered
    tc.generate_tasks(task_queue)

    # clear any remaining items from the queue
    task_queue.queue.clear()
    return 0