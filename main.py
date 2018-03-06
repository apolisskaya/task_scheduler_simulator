from Views import main_view as mv
from Controllers import task_controller as tc
from Controllers import simulator_controller as sc
from Models import cpu_model


PERFORMANCE_LOG_LOCATION = 'algorithm_performance.csv'

for i in range(3):
    sc.run_algorithm_simulation(algorithm=i+1, number_of_tasks=12, number_of_processors=4, number_of_cycles=5,
                                charging=True)

# TODO: temporarily commented out until view is fixed
# if PERFORMANCE_LOG_LOCATION:
#     mv.display_performance(PERFORMANCE_LOG_LOCATION)