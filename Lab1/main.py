import numpy as np
import RandomGenerator
import statistics
from MM1QueueSim import MM1QueueSim


def question1():
    print("**QUESTION 1**")
    Q1_LAMBDA = 75
    Q1_COUNT = 1000
    result = []
    for _ in range(Q1_COUNT):
        result.append(RandomGenerator.gen_exponential_val(Q1_LAMBDA))

    expected_mean = 1/Q1_LAMBDA
    expected_variance = 1/(Q1_LAMBDA**2)
    mean = statistics.mean(result)
    _variance = statistics.variance(result)
    print(f'Expected mean: {expected_mean}, Actual mean: {mean}')
    print(
        f'Expected variance: {expected_variance}, Actual variance: {_variance}')
    print("\n")


def m_m_1_queue():
    # rho values are 0.25 > to < 0.95 with a 0.1 step
    rho_values = [0.35, 0.45, 0.55, 0.65, 0.75, 0.85]
    sim_time_found = False
    time_multiplier = 1

    T = 1000
    L = 2000
    C = 1000000
    prev_en_values = []
    prev_p_idle_values = []
    en_values = []
    p_idle_values = []

    while not sim_time_found:
        for rho in rho_values:
            simulation = MM1QueueSim(time_multiplier*T, C, rho, L)
            simulation.run()

            en_values.append(simulation.en)
            p_idle_values.append(simulation.p_idle)

        if len(prev_en_values) > 0 and len(prev_p_idle_values) > 0:
            en_percent_diff_sum = 0
            p_idle_percent_diff_sum = 0
            for i in range(len(rho_values)):
                en_percent_diff_sum += 100 * \
                    abs(prev_en_values[i] - en_values[i]) / prev_en_values[i]
                p_idle_percent_diff_sum += 100 * \
                    abs(prev_p_idle_values[i] -
                        p_idle_values[i]) / prev_p_idle_values[i]

            avg_en_diff = en_percent_diff_sum / len(rho_values)
            avg_p_idle_diff = p_idle_percent_diff_sum / len(rho_values)
            print([avg_en_diff, avg_p_idle_diff])
            sim_time_found = True

        prev_en_values = en_values
        prev_p_idle_values = p_idle_values
        en_values = []
        p_idle_values = []
        time_multiplier += 1

    """
	Generate Packet Arrival
		lambda = rho * C / L
		T = 1000

	Generate Packet Length
		lambda = 1/2000
		num_lengths = num_arrivals
	
	Generate service time
		for each pkt(i), L(i) / C

    """

    """
        Generate packet departure
                if queue has packets. arrival pkt(i) >= departure(i - 1):
                        departure time pkt(i) = departure pkt(i-1) + service time pkt(i)
                else
                        departure time pkt(i) = arrival pkt(i) + service time pkt(i) 

        """

    """
	Generate Observer Events
		generate random observation events according to packet arrival distirbution
		rate of 5 times more than packet arrival
			- lambda * 5
		Observer Event - record state of queue:
			- E[N]: avg of num packets in queue (Na - Nd) / No
			- P_idle: proportion of time the server is idle (system is empty): is_idle = Na == Nd ? 1 : 0 
			- P_Loss: probability the packet will be dropped, due to buffer being full
	"""
    """
	Creating the DES?
		Put all events in a list and sort them by time
		Based on event type, increment Na, Nd, and No
			if event is observer, calculate the performance metrics
	"""


m_m_1_queue()
