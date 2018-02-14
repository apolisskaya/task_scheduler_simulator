from Views import main_view as mv
from Controllers import task_controller as tc
from Controllers import simulator_controller as sc
from Models import cpu_model

processor = cpu_model.Processor(power_available=40, power_max=50)
sc.run_algorithm_1_simulation(processor=processor, number_of_tasks=5)