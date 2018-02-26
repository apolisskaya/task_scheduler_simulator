import os, csv


def record_algorithm_performance(filepath, headings, data_to_record):
    try:
        current_filepath = filepath
        f = open(current_filepath, 'a+')
        csv_writer = csv.writer(f, delimiter=",")

        if file_is_empty(filepath=current_filepath):
            csv_writer.writerow(headings)

        csv_writer.writerow(data_to_record)

        f.close()

    except Exception as e:
        print('Something went wrong. Results not recorded.', str(e))


def file_is_empty(filepath):
    return os.stat(filepath).st_size == 0