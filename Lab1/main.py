import matplotlib.pyplot as plt
import RandomGenerator
import statistics
from MM1QueueSim import MM1QueueSim
from MM1KQueueSim import MM1KQueueSim


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

            if avg_en_diff <= 5 and avg_p_idle_diff <= 5:
                sim_time_found = True
                print("Precentage difference in results for T={} and T={} is less than 5%. Simulation is stable.".format(
                    T*(time_multiplier - 1), T*time_multiplier))

        prev_en_values = en_values
        prev_p_idle_values = p_idle_values
        en_values = []
        p_idle_values = []
        time_multiplier += 1


def m_m_1_k_queue():
    # rho values are 0.5 to 1.5
    rho_values = [0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
    k_values = [10, 25, 50]
    T = 1000
    L = 2000
    C = 1000000

    t = T

    en_data_10 = []
    p_loss_data_10 = []

    for rho in rho_values:
        sim = MM1KQueueSim(t, k_values[0], C, rho, L)
        sim.run()

        en_data_10.append(sim.en)
        p_loss_data_10.append(sim.p_loss)

    en_data_25 = []
    p_loss_data_25 = []

    for rho in rho_values:
        sim = MM1KQueueSim(t, k_values[1], C, rho, L)
        sim.run()

        en_data_25.append(sim.en)
        p_loss_data_25.append(sim.p_loss)

    en_data_50 = []
    p_loss_data_50 = []

    for rho in rho_values:
        sim = MM1KQueueSim(t, k_values[2], C, rho, L)
        sim.run()

        en_data_50.append(sim.en)
        p_loss_data_50.append(sim.p_loss)

    plt.scatter(rho_values, en_data_10)
    plt.scatter(rho_values, en_data_25)
    plt.scatter(rho_values, en_data_50)
    plt.show()
    plt.savefig('k_en_data.png')
    plt.clf()
    plt.scatter(rho_values, p_loss_data_10)
    plt.scatter(rho_values, p_loss_data_25)
    plt.scatter(rho_values, p_loss_data_50)
    plt.show()
    plt.savefig('k_p_loss_data.png')


def main():
    m_m_1_queue()
    # m_m_1_k_queue()


if __name__ == "__main__":
    main()
