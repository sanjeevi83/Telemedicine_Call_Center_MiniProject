import math

def calculate_utilization(arrival_rate, service_rate, servers):
    """
    Calculates system utilization (rho)
    """
    return arrival_rate / (servers * service_rate)


def erlang_c_probability(arrival_rate, service_rate, servers):
    """
    Calculates Erlang-C probability that a call has to wait
    """
    rho = arrival_rate / (servers * service_rate)

    sum_terms = 0
    for k in range(servers):
        sum_terms += (arrival_rate / service_rate) ** k / math.factorial(k)

    last_term = ((arrival_rate / service_rate) ** servers / math.factorial(servers)) * (1 / (1 - rho))
    p0 = 1 / (sum_terms + last_term)

    pw = last_term * p0
    return pw


def calculate_waiting_time(arrival_rate, service_rate, servers):
    """
    Calculates average waiting time in queue (Wq)
    """
    pw = erlang_c_probability(arrival_rate, service_rate, servers)
    wq = pw / (servers * service_rate - arrival_rate)
    return wq
