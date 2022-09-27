import numpy as np
import RandomGenerator
import statistics


def question1():
    print("**QUESTION 1**")
    Q1_LAMBDA = 75
    Q1_COUNT = 1000
    result = []
    for _ in range(Q1_COUNT):
        result.append(RandomGenerator.gen_exponential_val(Q1_LAMBDA))

    expected_mean = 1/75
    expected_variance = 1/(Q1_LAMBDA**2)
    mean = statistics.mean(result)
    _variance = statistics.variance(result)
    print(f'Expected mean: {expected_mean}, Actual mean: {mean}')
    print(
        f'Expected variance: {expected_variance}, Actual variance: {_variance}')
    print("\n")


def m_m_1_queue():
    # rho values are 0.25 to 0.95
    rho_values = [0.35, 0.45, 0.55, 0.65, 0.75, 0.85]
    T = 1000
    L = 2000
    C = 1000000

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
			- lammbda * 5
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


question1()
