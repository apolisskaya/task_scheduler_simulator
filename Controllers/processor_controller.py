from Models import cpu_model as cm


def generate_processors(number_of_processors, supercap):
    """
    :return: A list of processors
    """
    processor_list = []
    for i in range(number_of_processors):
        new_processor = cm.Processor(id=i, power_available=60, power_max=70)
        processor_list.append(new_processor)
        supercap.add_new_processor(new_processor)
    return processor_list