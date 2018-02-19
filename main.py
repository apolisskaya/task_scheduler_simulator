from Views import main_view as mv
from Controllers import task_controller as tc
from Controllers import simulator_controller as sc
from Models import cpu_model

# processor = cpu_model.Processor(power_available=40, power_max=50)

# TODO: Careful, processor will currently run out of juice if these are run back to back, comment out what is unused!
# sc.run_algorithm_1_simulation(processor=processor, number_of_tasks=5)
# sc.run_algorithm_2_simulation(processor=processor, number_of_tasks=5)
# sc.run_algorithm_3_simulation(processor=processor, number_of_tasks=5)


# Run each algorithm 5 times, take the average performance metrics.
# Number of tasks and power available to processor can be toggled here
# Deadline, execution time, and power consumption of tasks can be toggled in task_controller
completed_percentage_sum = 0.00
hit_deadline_sum = 0.00
awt_sum = 0.00
for i in range(5):
    processor = cpu_model.Processor(power_available=40, power_max=50)
    c, h, a = sc.run_algorithm_3_simulation(processor=processor, number_of_tasks=5)
    completed_percentage_sum += c
    hit_deadline_sum += h
    awt_sum += a

print('Completed: ', completed_percentage_sum / 5.0)
print('Hit Deadline: ', hit_deadline_sum / 5.0)
print('AWT: ', awt_sum / 5.0)