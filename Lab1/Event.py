class EventType:
    ARRIVAL = 1
    DEPARTURE = 2
    OBSERVER = 3


class Event:
    def __init__(self, type, time, packet_length=0):
        self.type = type
        self.time = time
        self.packet_length = packet_length


class K_Event:
    def __init__(self, type, time, packet_length=0):
        self.type = type
        self.time = time
        self.packet_length = packet_length

    def __lt__(self, other):
        return self.time < other.time

    def __eq__(self, other):
        return self.time == other.time
