from abc import abstractmethod, ABC


class Vehicle(ABC):
    WITH_CONDITIONER = None

    @abstractmethod
    def drive(self, distance: int):
        ...

    @abstractmethod
    def refuel(self, fuel):
        ...


class Car(Vehicle):
    WITH_CONDITIONER = 0.9

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int):
        fuel_needed = (self.fuel_consumption + Car.WITH_CONDITIONER) * distance
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    WITH_CONDITIONER = 1.6

    def __init__(self, fuel_quantity: int, fuel_consumption: int):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance: int):
        fuel_needed = (self.fuel_consumption + Truck.WITH_CONDITIONER) * distance
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        fuel_given = fuel * 0.95
        self.fuel_quantity += fuel_given

