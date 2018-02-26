import numpy as np
import matplotlib.pyplot as plt
import csv

from Services import logging_service as ls


def display_performance(filepath):
    try:

        if ls.file_is_empty(filepath=filepath):
            print('No data available to display. Check the logging file path!')
        else:
            current_filepath = filepath
            f = open(current_filepath, 'r')
            csv_reader = csv.reader(f, delimiter=",")

            NUMBER_OF_COLUMNS = 3
            ind = np.arange(NUMBER_OF_COLUMNS)  # x-locations for the bars
            width = 0.35  # width of each bar
            fig, ax = plt.subplots()

            colors = ['r', 'y', 'b']
            data = []
            rects = [ax.bar(ind + (i * width), data[i], width, color=colors[i % 3]) for i in range(NUMBER_OF_COLUMNS)]

            ax.set_ylabel('Percentages')
            ax.set_title('Algorithm Performance Comparison')
            ax.set_xticks(ind + width / 3)

            # ax.set_xticklabels(csv_reader.__next__()[0:NUMBER_OF_COLUMNS])
            # for row in csv_reader:
            #     print(row)


        f.close()

    except Exception as e:
        print('Main View: Something went wrong. Results not recorded.', str(e))


def autolabel(rects, ax):
    """
    Attach a text label above each bar displaying its height
    """
    for rect in rects:
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.05*height,
                '%d' % int(height),
                ha='center', va='bottom')