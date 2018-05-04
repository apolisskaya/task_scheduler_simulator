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


def generate_new_task(id=0, processor=None):
    # generate new tasks with variable power demand and priority, and variable deadline
    new_task = Task(cpu_demand=1, power_demand=random.randrange(1, 10), processor=processor,
                    priority=random.randrange(0,10), deadline=datetime.datetime.now() +
                    datetime.timedelta(seconds=random.randrange(25, 35)), execution_time=random.randrange(1, 5), id=id)
    return new_task


# takes in task and processor objects and links them
def assign_task_to_processor(task, processor):
    processor.set_current_task(task)
    task.begin_task()


def deep_copy_task_list(task_list, processor_list):
    new_task_list = []

    for task in task_list:
        print('task for deep copy. on processor ', task.on_processor)
        new_task = Task(cpu_demand=task.cpu_demand, power_demand=task.power_demand, priority=task.priority,
                        deadline=task.deadline, execution_time=task.execution_time, id=task.id,
                        processor=task.on_processor)
        print('new task created. on processor ', new_task.on_processor)
        new_task.origination_time = task.origination_time
        new_task.status = 0
        new_task.start_time = task.start_time
        new_task_list.append(new_task)
        new_task.hit_deadline = task.hit_deadline

    return new_task_list
