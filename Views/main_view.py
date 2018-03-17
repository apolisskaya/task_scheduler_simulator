# library
import matplotlib.pyplot as plt
import csv


def display_performance(file_path='algorithm_performance.csv', algorithm_count = 3):

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

    for algorithm in algorithm_performance_dict:
        for param in algorithm_performance_dict[algorithm]:
            param /= task_count
    f.close()

    # Create bars, these are the values of bars of each category/color
    # format will be: barsx = [completed %, deadline met &, awt] for algorithm x
    barWidth = 0.9
    bars1 = algorithm_performance_dict['1']
    bars2 = algorithm_performance_dict['2']
    bars3 = algorithm_performance_dict['3']
    bars4 = bars1 + bars2 + bars3

    print('bars1:', bars1)

    # order of the bars where r1 is for bars1, r2 for bars2, etc
    r1 = [1, 4, 7]
    r2 = [2, 5, 8]
    r3 = [3, 6, 9]
    r4 = r1 + r2 + r3

    # Create barplot
    plt.bar(r1, bars1, width=barWidth, color=(0.3, 0.1, 0.4), label='Algorithm 1')
    plt.bar(r2, bars2, width=barWidth, color=(0.3, 0.5, 0.4), label='Algorithm 2')
    plt.bar(r3, bars3, width=barWidth, color=(0.3, 0.9, 0.4), label='Algorithm 3')

    # Create legend
    plt.legend()

    # Text below each barplot with a rotation at 90°
    plt.xticks([r + (barWidth * 3) for r in range(3)],
               ['Task Completed', 'Deadline Hit', 'Average Waiting Time'], rotation=90)

    # Adjust the margins
    plt.subplots_adjust(bottom=0.2, top=0.98)

    # Show graphic
    plt.show()