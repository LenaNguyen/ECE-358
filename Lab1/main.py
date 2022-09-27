import numpy as np
import RandomGenerator


def m_m_1_queue():
    _lamdba = 75
    _arrive_time_number = 1000
    arrival_times = np.random.exponential(1/_lamdba, 1000)
