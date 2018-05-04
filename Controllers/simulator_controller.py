from multiprocessing import Process  # https://stackoverflow.com/questions/3474382/how-do-i-run-two-python-loops-concurrently
import queue, time, random, operator

from Controllers import task_controller as tc
from Controllers import processor_controller as pc
from Services import performance_service as ps
from Models import cpu_model as cm

# Main Controller for Simulations
# Contains different scheduling approaches
# May also end up containing performance evaluation metrics - should probably be in a different file

# For now, these will just run the simulation with all tasks sent to scheduler at the same time.

algorithm_dict = {
    1: operator.attrgetter('deadline', 'priority', 'execution_time'),
    2: operator.attrgetter('deadline', 'execution_time', 'priority'),
    3: operator.attrgetter('priority', 'deadline', 'execution_time'),
    4: operator.attrgetter('power_consumption_times_prio', 'power_demand', 'deadline'),
}


def process_tasks_in_queue(task_queue, solar_charging=False, charging_scale=1):
    completed_tasks, failed_tasks = [], []

    while not task_queue.empty():
        current_task = task_queue.get()
        # check that processor has enough juice to execute the task
        current_processor = current_task.get_processor()
        current_processor.get_supercap().switch_processor(current_processor)
        supercap = current_processor.get_supercap().battery
        if (current_task.power_demand < current_processor.battery.power_available) and \
                        current_processor.battery.power_available - current_task.power_demand > \
                        current_processor.battery.power_minimum and supercap and \
                        supercap.power_available - current_task.execution_time > supercap.power_minimum:
            # set processor to run current task and log start time of task for performance purposes
            tc.assign_task_to_processor(task=current_task, processor=current_processor)
            print('running task ', current_task.id, 'on processor', current_processor.id)
            time.sleep(current_task.execution_time)  # seconds
            # supercap should also lose charge here based on execution time
            current_task.get_processor().run_task(current_task)
            if solar_charging:
                current_processor.battery.charge_capacitor(current_task.execution_time * charging_scale)
                supercap.charge_capacitor(current_task.execution_time *
                                                                                     charging_scale)
            current_task.complete_task()
            completed_tasks.append(current_task)
        else:
            print('Capacitor power failure!')
            failed_tasks.append(current_task)

    return completed_tasks, failed_tasks


def run_algorithm_simulation(algorithm, number_of_tasks, number_of_cycles=1, solar_charging=False, number_of_processors=1,
                             tasks=None, processors=None, completed_tasks=[], failed_tasks=[]):
    if number_of_processors < 1 or number_of_tasks < 1 or algorithm not in algorithm_dict:
        print('Improper simulation call, check arguments and try again!')
        return -1
    else:
        if not processors or not tasks:
            supercap = cm.SuperCapacitor(power_available=200, power_max=250)
            processor_list = pc.generate_processors(number_of_processors, supercap)
            task_list = [tc.generate_new_task(id=i, processor=random.choice(processor_list)) for i in
                         range(0, number_of_tasks)]
        else:
            processor_list = [processor for processor in processors]
            task_list = tc.deep_copy_task_list(tasks, processor_list)

        task_queue = queue.Queue()

        task_list.sort(key=algorithm_dict[algorithm])
        for i in range(0, number_of_tasks):
            task_queue.put(task_list[i])
        completed_tasks_current_run, failed_tasks_current_run = process_tasks_in_queue(task_queue, solar_charging)

        task_queue.queue.clear()

        # if number of cycles is greater than zero, run again, with updated priorities
        if number_of_cycles > 0:
            for failed_task in failed_tasks:
                failed_task.change_priority(failed_task.get_priority() + 1)
            run_algorithm_simulation(algorithm, number_of_tasks, number_of_cycles - 1, solar_charging, number_of_processors,
                                       tasks=completed_tasks_current_run + failed_tasks_current_run, processors=processor_list,
                                       completed_tasks=tc.deep_copy_task_list(completed_tasks_current_run, processor_list) +
                                                       tc.deep_copy_task_list(completed_tasks, processor_list),
                                       failed_tasks=tc.deep_copy_task_list(failed_tasks_current_run, processor_list) +
                                                    tc.deep_copy_task_list(failed_tasks, processor_list))
        else:
            percent_completed, percent_hit_deadline, awt = ps.run_performance_evaluation(completed=completed_tasks,
                                                        failed=failed_tasks, algorithm=algorithm)

            print(str(percent_completed), 'completed, ', percent_hit_deadline, ' hit deadline, ', awt, ' awt')
            return percent_completed, percent_hit_deadline, awt