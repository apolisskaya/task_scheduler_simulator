import random, queue, datetime

from Models.task_model import Task
from Models.cpu_model import Processor


# generates tuples of tasks and some property of those tasks as specified by arg2
def generate_task_and_task_property_tuples(task_queue, task_property, tiebreaker, secondary_tiebreaker):
    for i in range(0, 20):
        new_task = generate_new_task()
        task_queue.put((new_task.__getattribute__(task_property), new_task))


def generate_tasks(task_queue):
    for i in range(0, 20):
        task_queue.put(generate_new_task())


def generate_new_task(id = 0):
    # generate new tasks with variable power demand and priority, and variable deadline
    new_task = Task(cpu_demand=1, power_demand=random.randrange(1, 10),
                    priority=random.randrange(0,10), deadline=datetime.datetime.now() +
                    datetime.timedelta(seconds=random.randrange(5, 10)), execution_time=random.randrange(1, 5), id=id)
    return new_task


# takes in task and processor objects and links them
def assign_task_to_processor(task, processor):
    processor.set_current_task(task)
    task.set_processor(processor)
