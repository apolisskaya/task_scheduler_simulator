import datetime, math
from Services import logging_service as ls


def run_performance_evaluation(completed, failed, algorithm, number_of_tasks):

    # Which tasks were and were not completed. To start, should be all tasks complete
    completed_task_ids, failed_task_ids = [str(task.id) for task in completed], [str(task.id) for task in failed]
    percent_completed = calculate_success_percentage(completed, failed)

    # Now we want to calculate our deadline hit/miss, and show it for each task
    hit_deadline, missed_deadline = [str(task.id) for task in completed if task.hit_deadline], \
                                    [str(task.id) for task in completed if not task.hit_deadline]
    missed_deadline += failed_task_ids

    percent_hit_deadline = calculate_success_percentage(hit_deadline, missed_deadline)
    wt_sum = math.fsum(datetime.timedelta.total_seconds(task.start_time - task.origination_time) for task in completed)
    awt = wt_sum / len(completed)

    ls.record_algorithm_performance('algorithm_performance.csv', ['Percent Completed', 'Percent Hit Deadline',
                                    'Average Waiting Time', 'Number of Tasks', 'Algorithm', 'Number of Tasks'],
                                    [percent_completed, percent_hit_deadline, awt, len(completed) + len(failed),
                                     algorithm, number_of_tasks])

    # Return the relevant statistics
    return percent_completed, percent_hit_deadline, awt


def calculate_success_percentage(success_list, failure_list):
    return float(len(success_list) / (len(success_list) + len(failure_list))) * 100.0
