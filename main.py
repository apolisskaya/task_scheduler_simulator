from Models.task_model import Task
from Models.cpu_model import Processor
from Views import main_view as mv

mv.init_main_view()

# sample class usage until controllers are set up

# example of an initialized task with cpu demand 300, power demand 500, priority 1 (lowest)
sample_task = Task(300, 500, 1)
# example of an initialized processor with 400 power available and 500 power max
sample_processor = Processor(400, 500)