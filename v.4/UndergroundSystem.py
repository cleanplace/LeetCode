import collections

class UndergroundSystem:

    def __init__(self):
        self.user = collections.defaultdict(list)
        self.dest = collections.defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.user[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, prev_time = self.user[id]
        self.dest[(start_station, stationName)].append(t - prev_time)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return float(sum(self.dest[(startStation, endStation)])) / len(self.dest[(startStation, endStation)])


