from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:

    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def __find_driver(self, driver_name: str):
        driver = [d for d in self.drivers if d.name == driver_name]
        if driver:
            return driver[0]

        return False

    def __find_race(self, race_name: str):
        race = [r for r in self.races if r.name == race_name]
        if race:
            return race[0]

        return False

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if model in [c.model for c in self.cars]:
            raise Exception(f'Car {model} is already created!')

        if car_type == 'MuscleCar':
            car = MuscleCar(model, speed_limit)
            self.cars.append(car)
            return f'{car_type} {model} is created.'

        elif car_type == 'SportsCar':
            car = SportsCar(model, speed_limit)
            self.cars.append(car)
            return f'{car_type} {model} is created.'

    def create_driver(self, driver_name: str):
        if driver_name in [d.name for d in self.drivers]:
            raise Exception(f'Driver {driver_name} is already created!')

        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f'Driver {driver_name} is created.'

    def create_race(self, race_name: str):
        if race_name in [r.name for r in self.races]:
            raise Exception(f'Race {race_name} is already created!')

        race = Race(race_name)
        self.races.append(race)
        return f'Race {race_name} is created.'

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver(driver_name)
        available_cars = [c for c in self.cars if c.__class__.__name__ == car_type and not c.is_taken]
        if not driver:
            raise Exception(f'Driver {driver_name} could not be found!')

        if not available_cars:
            raise Exception(f'Car {car_type} could not be found!')

        valid_car_types = ['MuscleCar', 'SportsCar']
        if car_type in valid_car_types:
            car = available_cars[-1]

            if driver.car:
                old_car = driver.car
                driver.car = car
                old_car.is_taken = False
                car.is_taken = True
                return f'Driver {driver_name} changed his car from {old_car.model} to {car.model}.'

            driver.car = car
            car.is_taken = True
            return f'Driver {driver_name} chose the car {car.model}.'

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__find_race(race_name)
        driver = self.__find_driver(driver_name)
        if not race:
            raise Exception(f'Race {race_name} could not be found!')

        if not driver:
            raise Exception(f'Driver {driver_name} could not be found!')

        if driver.car is None:
            raise Exception(f'Driver {driver_name} could not participate in the race!')

        if driver_name in [d.name for d in race.drivers]:
            return f'Driver {driver_name} is already added in {race_name} race.'

        race.drivers.append(driver)
        return f'Driver {driver_name} added in {race_name} race.'

    def start_race(self, race_name: str):
        race = self.__find_race(race_name)
        if not race:
            raise Exception(f'Race {race_name} could not be found!')

        if len(race.drivers) < 3:
            raise Exception(f'Race {race_name} cannot start with less than 3 participants!')

        sorted_drivers = sorted(race.drivers, key=lambda x: -x.car.speed_limit)
        first_place_driver = sorted_drivers[0]
        second_place_driver = sorted_drivers[1]
        third_place_driver = sorted_drivers[2]
        first_place_driver.number_of_wins += 1
        second_place_driver.number_of_wins += 1
        third_place_driver.number_of_wins += 1
        output = [
            f'Driver {first_place_driver.name} wins the {race_name} race with a speed of {first_place_driver.car.speed_limit}.',
            f'Driver {second_place_driver.name} wins the {race_name} race with a speed of {second_place_driver.car.speed_limit}.',
            f'Driver {third_place_driver.name} wins the {race_name} race with a speed of {third_place_driver.car.speed_limit}.',
        ]
        return '\n'.join(output)


# controller = Controller()
# print(controller.create_driver("Peter"))
# print(controller.create_car("SportsCar", "Porsche 718 Boxster", 470))
# print(controller.add_car_to_driver("Peter", "SportsCar"))
# print(controller.create_car("SportsCar", "Porsche 911", 580))
# print(controller.add_car_to_driver("Peter", "SportsCar"))
# print(controller.create_car("MuscleCar", "BMW ALPINA B7", 290))
# print(controller.create_car("MuscleCar", "Mercedes-Benz AMG GLA 45", 420))
# print(controller.create_driver("John"))
# print(controller.create_driver("Jack"))
# print(controller.create_driver("Kelly"))
# print(controller.add_car_to_driver("Kelly", "MuscleCar"))
# print(controller.add_car_to_driver("Jack", "MuscleCar"))
# print(controller.add_car_to_driver("John", "SportsCar"))
# print(controller.create_race("Christmas Top Racers"))
# print(controller.add_driver_to_race("Christmas Top Racers", "John"))
# print(controller.add_driver_to_race("Christmas Top Racers", "Jack"))
# print(controller.add_driver_to_race("Christmas Top Racers", "Kelly"))
# print(controller.add_driver_to_race("Christmas Top Racers", "Peter"))
# print(controller.start_race("Christmas Top Racers"))
# [print(d.name, d.number_of_wins) for d in controller.drivers]
