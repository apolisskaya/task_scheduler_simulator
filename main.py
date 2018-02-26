from Views import main_view as mv
from Controllers import task_controller as tc
from Controllers import simulator_controller as sc
from Models import cpu_model


PERFORMANCE_LOG_LOCATION = 'algorithm_performance.csv'

# Run each algorithm 5 times, take the average performance metrics.
# Number of tasks and power available to processor can be toggled here
# Deadline, execution time, and power consumption of tasks can be toggled in task_controller
completed_percentage_sum = 0.00
hit_deadline_sum = 0.00
awt_sum = 0.00
for i in range(5):
    processor = cpu_model.Processor(power_available=60, power_max=70)
    c, h, a = sc.run_algorithm_1_simulation(processor=processor, number_of_tasks=8)
    completed_percentage_sum += c
    hit_deadline_sum += h
    awt_sum += a

print('Completed: ', completed_percentage_sum / 5.0)
print('Hit Deadline: ', hit_deadline_sum / 5.0)
print('AWT: ', awt_sum / 5.0)

if PERFORMANCE_LOG_LOCATION:
    mv.display_performance(PERFORMANCE_LOG_LOCATION)


# TODO: code below to run simulation where multiple peripherals exist

# Starting sample code below
supercap = cpu_model.SuperCapacitor(power_available=150, power_max=200)
# add some peripherals to the supercap
for i in range(5):
    supercap.all_processors.append(cpu_model.Processor(power_available=60, power_max=70, id=i))

# this is where things get a bit more tricky. jobs can be on different peripherald, but should still be sorted as one list for scheduling
# TODO: is there any power cost to switching between peripherals?
# TODO: if not, is there any reason not to just treat this as a single peripheral with a single core processor?