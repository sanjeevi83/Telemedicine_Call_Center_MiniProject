def calculate_arrival_rate(data):
    """
    Calculates arrival rate (lambda) as:
    total number of calls / total observation time
    """
    total_calls = len(data)
    observation_time = data['arrival_time_min'].max()
    arrival_rate = total_calls / observation_time
    return arrival_rate
