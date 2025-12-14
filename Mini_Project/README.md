Telemedicine Call Center Performance Modeling – Mini Project 

Course

#EEX5362 – Performance Modeling and Evaluation


#Project Overview

This mini project presents a performance modeling and evaluation study of a telemedicine call center system. The system represents a healthcare service environment where patient calls arrive randomly and are handled by a limited number of medical support agents.

The objective of the project is to analyze key performance metrics such as patient waiting time, agent utilization, and system behavior under varying load conditions using queueing theory.

An analytical M/M/c queueing model is used to represent the system, and real call record data is analyzed using Python.



#System Description

In the telemedicine call center:

Patient calls arrive continuously throughout the observation period

Calls are served by multiple medical support agents

When all agents are busy, incoming calls wait in a queue

Calls are served on a first-come, first-served basis

The system performance is evaluated to identify bottlenecks and assess whether the current number of agents is sufficient to handle incoming demand.



#Dataset Description

The dataset used in this project is stored in CSV format and contains telemedicine call records.

File: telemedicine_call_data.csv

Columns:

call_id – Unique call identifier

arrival_time_min – Call arrival time (minutes from start)

service_time_min – Call service duration (minutes)

agent_id – Identifier of the handling agent

The dataset contains 30 call records collected over an observation period of approximately 57.9 minutes.



#Modeling Approach

The system is modeled using an M/M/c queueing model, where:

Arrival rate (λ) is calculated from the dataset

Service rate (μ) is calculated from average service time

c = 7 service agents are assumed


Key performance metrics evaluated include:

System utilization (ρ)

Average waiting time in the queue (Wq)


#Project Structure
Telemedicine_Call_Center_MiniProject/
│
├── analysis/
│   ├── data_loader.py
│   ├── arrival_rate_calculation.py
│   ├── service_rate_calculation.py
│   ├── queue_metrics_mm_c.py
│   ├── performance_plots.py
│   └── main_analysis.py
│
├── telemedicine_call_data.csv
├── Mini_Project_Report.pdf
└── README.md



#How to Run the Analysis

Install required Python libraries:

pip install pandas numpy matplotlib


Navigate to the analysis folder:

cd analysis


Run the main analysis script:

python main_analysis.py

py main_analysis.py


#Output

Running main_analysis.py produces:

Printed performance metrics:

	Arrival rate (λ)

	Service rate (μ)

	Utilization (ρ)

	Average waiting time (Wq)

A performance plot showing arrival rate vs average waiting time

The graph visually represents system behavior and congestion effects under increasing load.


#Conclusion

The results show that the telemedicine call center operates under stable conditions for the observed workload. However, as call arrival rates increase, waiting times rise sharply, indicating potential congestion during peak demand periods. The analysis highlights the importance of capacity planning in healthcare call centers.