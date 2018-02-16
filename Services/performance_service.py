import datetime, math


def run_performance_evaluation(completed, failed):
    # TODO: Format this to look a bit better

    # Which tasks were and were not completed. To start, should be all tasks complete
    completed_task_ids, failed_task_ids = [str(task.id) for task in completed], [str(task.id) for task in failed]
    # print('completed: ', completed_task_ids)
    # print('failed: ', failed_task_ids)
    percent_completed = calculate_success_percentage(completed, failed)
    print(percent_completed, ' percent completed')

    # Now we want to calculate our deadline hit/miss, and show it for each task
    hit_deadline, missed_deadline = [str(task.id) for task in completed if task.hit_deadline], \
                                    [str(task.id) for task in completed if not task.hit_deadline]
    missed_deadline += failed_task_ids
    # print('hit deadline: ', hit_deadline)
    # print('missed deadline: ', missed_deadline)
    percent_hit_deadline = calculate_success_percentage(hit_deadline, missed_deadline)
    print(percent_hit_deadline, ' percent hit deadline')

    wt_sum = math.fsum(datetime.timedelta.total_seconds(task.start_time - task.origination_time) for task in completed)
    awt = wt_sum / len(completed)
    print('Average Waiting Time: ', awt)

    # TODO: how to calculate and display throughput here?? Still seems irrelevant

    # Return the relevant statistics
    return percent_completed, percent_hit_deadline, awt


def calculate_success_percentage(success_list, failure_list):
    return float(len(success_list) / (len(success_list) + len(failure_list))) * 100.0
