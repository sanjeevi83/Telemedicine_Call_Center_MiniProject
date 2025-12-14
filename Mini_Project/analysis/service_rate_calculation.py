def calculate_service_rate(data):
    """
    Calculates service rate (mu) as:
    1 / average service time
    """
    average_service_time = data['service_time_min'].mean()
    service_rate = 1 / average_service_time
    return service_rate
