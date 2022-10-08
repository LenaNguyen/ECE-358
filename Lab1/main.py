import matplotlib.pyplot as plt
import RandomGenerator
from Stats import mean, variance
from MM1QueueSim import MM1QueueSim
from MM1KQueueSim import MM1KQueueSim
import argparse


def question1():
    print("**QUESTION 1**")
    Q1_LAMBDA = 75
    Q1_COUNT = 1000
    result = []
    for _ in range(Q1_COUNT):
        result.append(RandomGenerator.gen_exponential_val(Q1_LAMBDA))

    expected_mean = 1/Q1_LAMBDA
    expected_variance = 1/(Q1_LAMBDA**2)
    m = mean(result)
    _variance = variance(result)
    print(f'Expected mean: {expected_mean}, Actual mean: {m}')
    print(
        f'Expected variance: {expected_variance}, Actual variance: {_variance}')
    print("\n")


def m_m_1_queue():
    print("**QUESTION 3**")
    # rho values are 0.25 > to < 0.95 with a 0.1 step
    rho_values = [0.25, 0.35, 0.45, 0.55, 0.65, 0.75, 0.85, 0.95]
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

        if len(prev_en_values) > 0:
            sim_time_found = True
            for i in range(len(rho_values)):
                en_diff = float(
                    100 * abs(prev_en_values[i] - en_values[i]) / prev_en_values[i])

                if (en_diff > 5):
                    sim_time_found = False
                    break

        if (sim_time_found):
            time_multiplier -= 1
        else:
            time_multiplier += 1
        prev_en_values = en_values
        prev_p_idle_values = p_idle_values
        en_values = []
        p_idle_values = []

    print("Precentage difference in results for T={} and T={} is less than 5%. Simulation is stable.".format(
        T*time_multiplier, T*(time_multiplier + 1)))
    plt.title("Average number of packets in the buffer/queue over utilization of the queue in M/M/1 queue",
              loc='center', wrap=True)
    plt.plot(rho_values, prev_en_values)
    plt.xlabel("Utilization of the queue")
    plt.ylabel("Average number of packets in the buffer/queue")
    plt.grid()
    plt.savefig('./Lab1/en_data.png')
    plt.clf()

    plt.title("Proportion of time the server is idle over utilization of the queue in M/M/1 queue",
              loc='center', wrap=True)
    plt.plot(rho_values, prev_p_idle_values)
    plt.xlabel("Utilization of the queue")
    plt.ylabel("Proportion of time the server is idle")
    plt.grid()
    plt.savefig('./Lab1/p_idle_data.png')
    plt.clf()
    print("\n")


def question4():
    print("**QUESTION 4**")
    T = 2000
    L = 2000
    C = 1000000
    rho = 1.2
    simulation = MM1QueueSim(T, C, rho, L)
    simulation.run()
    print("\n")


def m_m_1_k_queue():
    print("**QUESTION 6**")
    # rho values are 0.5 to 1.5
    rho_values = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
    k_values = [10, 25, 50]
    T = 1000
    L = 2000
    C = 1000000

    min_T = 200
    time_multiplier = 1

    for k in k_values:
        prev_en_values = []
        en_values = []
        sim_time_found = False
        while not sim_time_found:

            for rho in rho_values:
                sim1 = MM1KQueueSim(min_T * time_multiplier, k, C, rho, L)
                sim1.run()
                en_values.append(sim1.en)

            if len(prev_en_values) > 0:
                sim_time_found = True
                for i in range(len(rho_values)):
                    en_diff = float(
                        100 * abs(prev_en_values[i] - en_values[i]) / prev_en_values[i])

                    if (en_diff > 5):
                        sim_time_found = False
                        break

            if (sim_time_found):
                time_multiplier -= 1
            else:
                time_multiplier += 1
            prev_en_values = en_values
            en_values = []

    print("Precentage difference in results for T={} and T={} is less than 5%. Simulation is stable.".format(
        min_T*time_multiplier, min_T*(time_multiplier+1)))

    # the smallest T is 1000
    if (min_T * time_multiplier) < T:
        print("Smallest experimental T=1000. \n Since simulation is stable for T < 1000, it will be stable for T=1000")

    T = max(min_T * time_multiplier, T)

    en_data_10 = []
    p_loss_data_10 = []

    for rho in rho_values:
        sim = MM1KQueueSim(T, k_values[0], C, rho, L)
        sim.run()

        en_data_10.append(sim.en)
        p_loss_data_10.append(sim.p_loss)

    en_data_25 = []
    p_loss_data_25 = []

    for rho in rho_values:
        sim = MM1KQueueSim(T, k_values[1], C, rho, L)
        sim.run()

        en_data_25.append(sim.en)
        p_loss_data_25.append(sim.p_loss)

    en_data_50 = []
    p_loss_data_50 = []

    for rho in rho_values:
        sim = MM1KQueueSim(T, k_values[2], C, rho, L)
        sim.run()

        en_data_50.append(sim.en)
        p_loss_data_50.append(sim.p_loss)

    plt.title("Average number of packets in the buffer/queue over utilization of the queue in M/M/1/K queue",
              loc='center', wrap=True)
    plt.plot(rho_values, en_data_10, label="K=10")
    plt.plot(rho_values, en_data_25, label="K=25")
    plt.plot(rho_values, en_data_50, label="K=50")
    plt.xlabel("Utilization of the queue")
    plt.ylabel("Average number of packets in the buffer/queue")
    plt.legend(loc="upper left")
    plt.grid()
    plt.savefig('./Lab1/k_en_data.png')
    plt.clf()

    plt.title("Packet loss probability over utilization of the queue in M/M/1/K queue",
              loc='center', wrap=True)
    plt.plot(rho_values, p_loss_data_10, label="K=10")
    plt.plot(rho_values, p_loss_data_25, label="K=25")
    plt.plot(rho_values, p_loss_data_50, label="K=50")
    plt.xlabel("Utilization of the queue")
    plt.ylabel("Packet loss probability")
    plt.legend(loc="upper left")
    plt.grid()
    plt.savefig('./Lab1/k_p_loss_data.png')
    plt.clf()
    print("\n")


def main():
    parser = argparse.ArgumentParser(description='ECE 358 Lab 1 DES')
    parser.add_argument('-Q1', '--question1', action='store_true',
                        help='Execute question 1')
    parser.add_argument('-Q3', '--question3', action='store_true',
                        help='Execute question 3')
    parser.add_argument('-Q4', '--question4', action='store_true',
                        help='Execute question 4')
    parser.add_argument('-Q6', '--question6', action='store_true',
                        help='Execute question 6')

    args = parser.parse_args()

    if args.question1:
        question1()
        exit()
    elif args.question3:
        m_m_1_queue()
        exit()
    elif args.question4:
        question4()
        exit()
    else:
        m_m_1_k_queue()


if __name__ == "__main__":
    main()
