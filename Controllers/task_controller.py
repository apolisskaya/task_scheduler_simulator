import random, queue, datetime

from Models.task_model import Task
from Models.cpu_model import Processor


def generate_tasks(task_queue):
    for i in range(0, 20):
        task_queue.put(generate_new_task())


def generate_new_task():
    # generate new tasks with variable power demand and priority, and variable deadline
    new_task = Task(cpu_demand=1, power_demand=random.randrange(0, 10),
                    priority=random.randrange(0,10), deadline=datetime.datetime.now() +
                                                              datetime.timedelta(seconds=random.randrange(1, 5)))
    return new_task


# takes in task and processor objects and links them
def assign_task_to_processor(task, processor):
    processor.set_current_task(task)
    task.set_processor(processor)
