

class ElectricCar:

    def __init__(self, max_range):
        self.max_range = max_range
        self.possible_distance = max_range

    def drive(self, distance):
        if distance >= self.possible_distance:
            can_travel = self.possible_distance
            self.possible_distance = 0
            return can_travel

        self.possible_distance -= distance

        return distance

    def charge(self):
        self.possible_distance = self.max_range


def test_electric_car():
    car = ElectricCar(100)
    assert car.drive(70) == 70
    assert car.drive(50) == 30
    assert car.drive(50) == 0
    car.charge()
    assert car.drive(50) == 50
    car.charge()
    assert car.drive(120) == 100
