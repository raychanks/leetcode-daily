class UndergroundSystem:
    def __init__(self):
        self.timing_info = {}
        self.check_ins = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_ins[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        check_in_station, check_in_time = self.check_ins[id]
        time_taken = t - check_in_time
        locations = (check_in_station, stationName)

        if locations in self.timing_info:
            timing_info = self.timing_info[locations]
            self.timing_info[locations] = (
                timing_info[0] + time_taken,
                timing_info[1] + 1,
            )
        else:
            self.timing_info[locations] = (time_taken, 1)

        del self.check_ins[id]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        locations = (startStation, endStation)
        timing_info = self.timing_info[locations]

        return timing_info[0] / timing_info[1]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
