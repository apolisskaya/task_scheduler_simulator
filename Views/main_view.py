# library
import matplotlib.pyplot as plt
import csv

from Services import display_service as ds


def display_performance(file_path, algorithm_count = 4):

    """
    We want the following for each of 3 algorithms:
    - AWT
    - Deadline Met %
    - Completed %
    """

    current_filepath = file_path
    f = open(current_filepath, 'r')
    csv_reader = csv.reader(f, delimiter=",")
    algorithm_performance_dict = {}
    for algorithm in range(1, algorithm_count+1, 1):
        algorithm_performance_dict[str(algorithm)] = [0 for i in range(3)]

    task_count = 0
    for row in csv_reader:
        if row != [] and row[4] != 'Algorithm':
            for i in range(3):
                algorithm_performance_dict[row[4]][i] += float(row[i])
            task_count += int(row[3])

    f.close()

    algorithm_performance_dict = ds.normalize_display(algorithm_performance_dict)

    # Create bars, these are the values of bars of each category/color
    # format will be: barsx = [completed %, deadline met &, awt] for algorithm x
    barWidth = 0.9
    bars = [algorithm_performance_dict[i] for i in list(algorithm_performance_dict)]

    # order of the bars where r1 is for bars1, r2 for bars2, etc
    r = [[i, i + algorithm_count, i + (2 * algorithm_count)] for i in range(algorithm_count)]

    # Create barplot
    plt.bar(r[0], bars[0], width=barWidth, color=(0.3, 0.1, 0.4), label='Algorithm 1')
    plt.bar(r[1], bars[1], width=barWidth, color=(0.3, 0.5, 0.4), label='Algorithm 2')
    plt.bar(r[2], bars[2], width=barWidth, color=(0.3, 0.9, 0.4), label='Algorithm 3')
    plt.bar(r[3], bars[3], width=barWidth, color=(0.2, 0.5, 0.7), label="Algorithm 4")

    # Create legend
    plt.legend()

    # Text below each barplot with a rotation at 90°
    plt.xticks([(r+1) * (barWidth * 3) for r in range(3)],
               ['Task Completed', 'Deadline Hit', 'Average Waiting Time'], rotation=90)

    # Adjust the margins
    plt.subplots_adjust(bottom=0.2, top=0.98)

    # Show graphic
    plt.show()