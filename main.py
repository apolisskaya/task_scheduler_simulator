from Views import main_view as mv
from Controllers import task_controller as tc
from Controllers import simulator_controller as sc
from Models import cpu_model


PERFORMANCE_LOG_LOCATION = 'algorithm_performance.csv'
algorithm_count = 3

for i in range(algorithm_count):
    sc.run_algorithm_simulation(algorithm=i+1, number_of_tasks=8, number_of_processors=2, number_of_cycles=5,
                                solar_charging=True)

if PERFORMANCE_LOG_LOCATION:
    mv.display_performance('algorithm_performance.csv', algorithm_count=algorithm_count)
