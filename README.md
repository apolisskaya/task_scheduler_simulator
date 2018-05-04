**Task Scheduling Simulator 1.0.0**

FAU I-SENSE 2018

https://github.com/apolisskaya

**Bsckground Info**

We are given some network of peripheral devices operated remotely via a single core microprocessor.
The microprocessor is powered by a supercapacitor, and each peripheral device is powered by its own dedicated capacitor.
Because all devices in the network are wireless and run on a finite fuel supply, the scheduling algorithm must be energy aware.

**Performance Metrics**

% Completed: What percentage of tasks are executed? If we do not have time to run a task, its execution is skipped. Each skipped task lowers the completion metric.

% Completed by Deadline: What percentage of tasks are completed by their specified deadline?

Average Waiting Time: The amount of time, on average, that a task spends in the queue prior to starting execution.

A common performance metric is throughput. Because this project assumes a small list of tasks per cycle, with the nature of the tasks unchanged between cycles, we choose to ignore it in our performance evaluation.

**Simulation Structure**

This simulation was built using the well known MVC paradigm. Models, which contain blueprints for the task and processor objects, are available under Models.
All methods utilizing these models to perform simulation tasks are located under Controllers. Methods used in the simulation that are "helper" methods are located under Services.
Finally, the code used to display the graph at the end of the simulation is located under Views.

**Algorithms**

_Algorithm 1:_ Earliest Deadline First Version 1. We sort the tasks for a given cycle, with the tasks having earlier deadlines in front of tasks having later deadlines. If two tasks have the same deadline, the task with a higher priority value takes priority. If two tasks share a deadline and have the same priority value, the task with an earlier execution time goes first. If two tasks share all three of these properties, the order does not matter.

_Algorithm 2:_ Earliest Deadline First Version 2. Same as above, but priority and execution time switch (we sort by execution time second and priority third).

_Algorithm 3:_ Highest Priority First. Sort tasks based on their priority value, with highest priority tasks executed first. If two tasks share a priority value, the task with the earlier deadline goes first. If two tasks share a priority value and a deadline, the task with the lowest execution time goes first. If all three properties are shared, order does not matter.

_Algorithm 4:_ Power Consumption and Priority based Algorithm. Taska are sorted by multiplying together the task's priority value and the multiplicative inverse of its power consumption. If this value is the same for two tasks we sort by power demand of the task, then deadline.

Once the tasks are sorted and placed into a Queue, they are handled one at a time starting with the front of the queue. A check is performed to make sure that both the peripheral and microcontroller have enough energy to run the task. If so, it is executed. If not, its priority value is incremented and it is skipped.

**Performance**

The simulation can be executed by running main.py. The software will generate a graph comparing the algorithms. For best results, run the simulation multiple times. A file called algorithm_peformance.csv will also be generated/updated in the same directory as main.py.
More information on CSV is available here: https://en.wikipedia.org/wiki/Comma-separated_values
The right-most column specifies which algorithm was used to generate that row. The other columns specify the values of each performance metric listed above and the number of tasks used for the calculation. If 8 tasks were run for 5 cycles, Number of Tasks will be 40.

