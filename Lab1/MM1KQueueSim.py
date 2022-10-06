from Event import EventType, K_Event
import RandomGenerator
import heapq

O_MULTIPLIER = 5

class MM1KQueueSim:
    def __init__(self, simulation_time, K, transmission_rate, utilization, avg_length):
        self.__arrivals = []
        self.__observers = []
        self.__all_events = []
        self.p_loss = 0
        self.en = 0
        self.T = simulation_time
        self.C = transmission_rate
        self.rho = utilization
        self.L = avg_length
        self.K = K

    def gen_arrivals(self):
        _lambda = self.rho * self.C / self.L
        # **Generate Arrivals**
        # populate with first event to avoid indexing issues
        increment = RandomGenerator.gen_exponential_val(_lambda)
        packet_length = RandomGenerator.gen_exponential_val(1/self.L)
        self.__arrivals.append(
            K_Event(EventType.ARRIVAL, increment, 0, packet_length))

        # generate arrival events until the last event time is greater than simulation time
        # for each arrival, generate a packet length
        while self.__arrivals[-1].time <= self.T:
            increment = RandomGenerator.gen_exponential_val(_lambda)
            packet_length = RandomGenerator.gen_exponential_val(1/self.L)

            event = K_Event(EventType.ARRIVAL,
                            self.__arrivals[-1].time + increment, len(self.__arrivals), packet_length)
            self.__arrivals.append(event)

        # Remove last event because it exceeds T
        self.__arrivals.pop

    def gen_departures(self, curr_time, event):
        # **Generate Departures**
        # populate the first departure to avoid indexing issues
        time = curr_time + (event.packet_length / self.C)
        return K_Event(EventType.DEPARTURE, time)

    def gen_observers(self):
        _lambda = self.rho * self.C / self.L
        # **Generate Observers**
        # populate first observer to avoid indexing issues
        time = RandomGenerator.gen_exponential_val(_lambda*O_MULTIPLIER)
        self.__observers.append(K_Event(EventType.OBSERVER, time))

        # generate observer events until the last event time is greater than target time
        while self.__observers[-1].time <= self.T:
            time = self.__observers[-1].time + \
                RandomGenerator.gen_exponential_val(_lambda*O_MULTIPLIER)
            self.__observers.append(K_Event(EventType.OBSERVER, time))

        # Remove last event because it exceeds T
        self.__observers.pop

    def process_events(self):
        na = 0
        nd = 0
        no = 0
        packets_in_queue = 0
        loss_count = 0
        q = 0
        curr_departure = 0

        # loop through each event in the sorted list
        while len(self.__all_events) > 0:
            event = heapq.heappop(self.__all_events)
            if (event.type == EventType.ARRIVAL):
                na += 1
                if (q < self.K):
                    service_time = event.packet_length / self.C
                    if (event.time > curr_departure):
                        curr_departure = event.time
                    curr_departure += service_time
                    heapq.heappush(self.__all_events, K_Event(
                        EventType.DEPARTURE, curr_departure))
                    q += 1
                else:
                    loss_count += 1
            elif (event.type == EventType.DEPARTURE):
                nd += 1
                q -= 1
            else:
                no += 1
                packets_in_queue += q

        self.en = packets_in_queue / no
        self.p_loss = loss_count / na

    def run(self):
        print("Running MM1K Queue Simulation for T={}, K={}, and rho={}".format(
            self.T, self.K, self.rho))
        self.gen_arrivals()
        self.gen_observers()

        for event in self.__arrivals:
            heapq.heappush(self.__all_events, event)
        for event in self.__observers:
            heapq.heappush(self.__all_events, event)

        self.process_events()
        print("E[N]={}  P_loss={}".format(self.en, self.p_loss))
