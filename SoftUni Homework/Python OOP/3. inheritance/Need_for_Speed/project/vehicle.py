class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel: float, horse_power: int):
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION
        self.fuel = fuel
        self.horse_power = horse_power

    def drive(self, kilometers: int):
        fuel_needed = (self.fuel_consumption * kilometers)

        if self.fuel - fuel_needed >= 0:
            self.fuel -= fuel_needed
