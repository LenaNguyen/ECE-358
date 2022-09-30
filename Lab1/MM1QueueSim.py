from Event import EventType, Event
import RandomGenerator
import matplotlib.pyplot as plt

O_MULTIPLIER = 5


class MM1QueueSim:
    __arrivals = []
    __test = []  # TODO: Remove
    __departures = []
    __observers = []
    __all_events = []
    p_idle = 0
    en = 0

    def __init__(self, simulation_time, transmission_rate, utilization, avg_length):
        self.T = simulation_time
        self.C = transmission_rate
        self.rho = utilization
        self.L = avg_length

    def gen_arrivals(self):
        _lambda = self.rho * self.C / self.L
        # **Generate Arrivals**
        # populate with first event to avoid indexing issues
        increment = RandomGenerator.gen_exponential_val(_lambda)
        self.__arrivals.append(Event(EventType.ARRIVAL, increment))
        self.__test.append(increment)

        # generate arrival events until the last event time is greater than simulation time
        # for each arrival, generate a packet length
        while self.__arrivals[-1].time <= self.T:
            increment = RandomGenerator.gen_exponential_val(_lambda)
            packet_length = RandomGenerator.gen_exponential_val(1/self.L)

            # TODO: Remove
            self.__test.append(increment)

            event = Event(EventType.ARRIVAL,
                          self.__arrivals[-1].time + increment, packet_length)
            self.__arrivals.append(event)

        # Remove last event because it exceeds T
        self.__arrivals.pop

    def gen_departures(self):
        # **Generate Departures**
        # populate the first departure to avoid indexing issues
        event = self.__arrivals[0]
        time = event.time + (event.packet_length / self.C)
        self.__departures.append(Event(EventType.DEPARTURE, time))

        # generate a departure for each arrival
        for i in range(1, len(self.__arrivals)):
            service_time = self.__arrivals[i].packet_length / self.C

            # when queue is empty
            if self.__arrivals[i].time >= self.__departures[i-1].time:
                time = self.__arrivals[i].time + service_time
            # when the queue is not empty
            else:
                time = self.__departures[i-1].time + service_time

            self.__departures.append(Event(EventType.DEPARTURE, time))

        # Remove last event because it exceeds T
        self.__departures.pop

    def gen_observers(self):
        _lambda = self.rho * self.C / self.L
        # **Generate Observers**
        # populate first observer to avoid indexing issues
        time = RandomGenerator.gen_exponential_val(_lambda*O_MULTIPLIER)
        self.__observers.append(Event(EventType.OBSERVER, time))

        # generate observer events until the last event time is greater than target time
        while self.__observers[-1].time <= self.T:
            time = self.__observers[-1].time + \
                RandomGenerator.gen_exponential_val(_lambda*O_MULTIPLIER)
            self.__observers.append(Event(EventType.OBSERVER, time))

        # Remove last event because it exceeds T
        self.__observers.pop

    def process_events(self):
        na = 0
        nd = 0
        no = 0
        packets_in_queue = 0
        idle_count = 0

        # loop through each event in the sorted list
        for event in self.__all_events:
            if event.type == EventType.ARRIVAL:
                na += 1
            elif event.type == EventType.DEPARTURE:
                nd += 1
            else:
                no += 1
                # check number of packets in the queue
                cur_packets_in_queue = na - nd
                if cur_packets_in_queue == 0:
                    idle_count += 1
                else:
                    packets_in_queue += cur_packets_in_queue

        self.en = packets_in_queue / no
        self.p_idle = idle_count / no
        print("process_events")
        print([self.en, self.p_idle])

    def run(self):
        self.gen_arrivals()
        self.gen_departures()
        self.gen_observers()
        self.__all_events = self.__arrivals + self.__departures + self.__observers
        self.__all_events.sort(key=lambda e: e.time)
        self.process_events()
