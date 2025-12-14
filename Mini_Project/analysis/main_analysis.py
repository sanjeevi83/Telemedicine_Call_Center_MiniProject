from data_loader import load_data
from arrival_rate_calculation import calculate_arrival_rate
from service_rate_calculation import calculate_service_rate
from queue_metrics_mm_c import calculate_utilization, calculate_waiting_time
from performance_plots import plot_waiting_time_vs_arrival

# Load dataset
data = load_data("../dataset/telemedicine_call_data.csv")

# Calculate parameters
arrival_rate = calculate_arrival_rate(data)
service_rate = calculate_service_rate(data)

# Number of agents
servers = 7

# Calculate performance metrics
utilization = calculate_utilization(arrival_rate, service_rate, servers)
waiting_time = calculate_waiting_time(arrival_rate, service_rate, servers)

# Display results
print("Arrival rate (λ):", round(arrival_rate, 3), "calls/min")
print("Service rate (μ):", round(service_rate, 3), "calls/min")
print("Utilization (ρ):", round(utilization, 3))
print("Average waiting time (Wq):", round(waiting_time, 3), "minutes")

# Generate plot
plot_waiting_time_vs_arrival(arrival_rate, service_rate, servers)
