class ParkingSystem:
    def __init__(self, big: int, medium: int, small: int):
        self._parking_slots = [0, big, medium, small]

    def addCar(self, carType: int) -> bool:
        if self._parking_slots[carType] > 0:
            self._parking_slots[carType] -= 1
            return True

        return False


# Your ParkingSystem object will be instantiated and called as such:
# obj = ParkingSystem(big, medium, small)
# param_1 = obj.addCar(carType)
