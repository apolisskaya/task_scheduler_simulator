def run_performance_evaluation(completed, failed):
    # TODO: Format this to look a bit better

    # Which tasks were and were not completed. To start, should be all tasks complete
    completed_task_ids, failed_task_ids = [str(task.id) for task in completed], [str(task.id) for task in failed]
    print('completed: ', completed_task_ids)
    print('failed: ', failed_task_ids)

    # Now we want to calculate our deadline hit/miss, and show it for each task
    hit_headline, missed_deadline = [str(task.id) for task in completed if task.hit_deadline], \
                                    [str(task.id) for task in completed if not task.hit_deadline]
    missed_deadline += failed_task_ids
    print('hit deadline: ', hit_headline)
    print('missed deadline: ', missed_deadline)

    # TODO: average waiting time of tasks


    # TODO: how to calculate and display throughput here?? Still seems irrelevant


def calculate_success_percentage(success_list, failure_list):
    return 0