import matplotlib.pyplot as plt # type: ignore
import numpy as np # type: ignore

def plot_waiting_time_vs_arrival(arrival_rate, service_rate, servers):
    """
    Plots average waiting time versus arrival rate
    """
    arrival_rates = np.linspace(0.3, arrival_rate * 1.2, 20)
    waiting_times = []

    for lam in arrival_rates:
        rho = lam / (servers * service_rate)
        if rho >= 1:
            waiting_times.append(None)
        else:
            wq = rho / (servers * service_rate * (1 - rho))
            waiting_times.append(wq)

    plt.figure()
    plt.plot(arrival_rates, waiting_times, marker='o')
    plt.xlabel("Arrival Rate (calls per minute)")
    plt.ylabel("Average Waiting Time (minutes)")
    plt.title("Waiting Time vs Arrival Rate")
    plt.grid(True)
    plt.show()
