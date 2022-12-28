from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    successful_missions = 0
    unsuccessful_missions = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def add_astronaut(self, astronaut_type: str, name: str):
        valid_types = ['Biologist', 'Geodesist', 'Meteorologist']
        if astronaut_type not in valid_types:
            raise Exception('Astronaut type is not valid!')

        if self.astronaut_repository.find_by_name(name):
            return f'{name} is already added.'

        if astronaut_type == 'Biologist':
            astronaut = Biologist(name)
            self.astronaut_repository.astronauts.append(astronaut)

        elif astronaut_type == 'Geodesist':
            astronaut = Geodesist(name)
            self.astronaut_repository.astronauts.append(astronaut)

        elif astronaut_type == 'Meteorologist':
            astronaut = Meteorologist(name)
            self.astronaut_repository.astronauts.append(astronaut)

        return f'Successfully added {astronaut_type}: {name}.'

    def add_planet(self, name: str, items: str):
        if self.planet_repository.find_by_name(name):
            return f'{name} is already added.'

        materials = items.split(', ')
        planet = Planet(name)
        for m in materials:
            planet.items.append(m)

        self.planet_repository.planets.append(planet)
        return f'Successfully added Planet: {name}.'

    def retire_astronaut(self, name: str):
        astronaut = self.astronaut_repository.find_by_name(name)
        if astronaut is None:
            raise Exception(f"Astronaut {name} doesn't exist!")

        self.astronaut_repository.astronauts.remove(astronaut)
        return f'Astronaut {name} was retired!'

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.increase_oxygen(10)

    def send_on_mission(self, planet_name: str):
        planet = self.planet_repository.find_by_name(planet_name)
        if planet is None:
            raise Exception('Invalid planet name!')

        capable_astronauts = [a for a in self.astronaut_repository.astronauts if a.oxygen > 30]
        if not capable_astronauts:
            raise Exception('You need at least one astronaut to explore the planet!')

        sorted_astronauts = sorted(capable_astronauts, key=lambda x: -x.oxygen)
        if len(sorted_astronauts) > 5:
            sorted_astronauts = sorted_astronauts[:5]

        astronauts_to_explore = 0
        for astronaut in sorted_astronauts:
            astronauts_to_explore += 1
            while astronaut.oxygen > 0:
                item_taken = planet.items.pop()
                astronaut.backpack.append(item_taken)
                astronaut.breathe()

                if not planet.items:
                    SpaceStation.successful_missions += 1
                    return f'Planet: {planet_name} was explored. {astronauts_to_explore}' \
                           f' astronauts participated in collecting items.'

        SpaceStation.unsuccessful_missions += 1
        return f'Mission is not completed.'

    def report(self):
        output = [
            f'{SpaceStation.successful_missions} successful missions!',
            f'{SpaceStation.unsuccessful_missions} missions were not completed!',
            "Astronauts' info:",
            ]

        for astronaut in self.astronaut_repository.astronauts:
            backpack_items = ', '.join(astronaut.backpack) if astronaut.backpack else 'none'
            info = f'Name: {astronaut.name}\n' \
                   f'Oxygen: {astronaut.oxygen}\n' \
                   f'Backpack items: {backpack_items}'
            output.append(info)

        return '\n'.join(output)


# app = SpaceStation()
# biologist = Biologist('Neil')
# geodesist = Geodesist('Jury')
# meteorologist = Meteorologist('Kobe')
# app.add_astronaut('Biologist', 'Diyan')
# app.add_astronaut('Meteorologist', 'Mitko')
# app.add_astronaut('Meteorologist', 'Sasho')
#
# # app.astronaut_repository.astronauts.append(biologist)
# # app.astronaut_repository.astronauts.append(geodesist)
# # app.astronaut_repository.astronauts.append(meteorologist)
#
# planet_mars = Planet('Mars')
# planet_mars.items.extend(['Diamonds', 'Gold', 'Silver', 'Bronze', 'Copper', 'Cyanide', 'Iron'])
# planet_mars.items.extend(['Diamonds', 'Gold', 'Silver', 'Bronze', 'Copper', 'Cyanide', 'Iron'])
# planet_mars.items.extend(['Diamonds', 'Gold', 'Silver', 'Bronze', 'Copper', 'Cyanide', 'Iron'])
# planet_mars.items.extend(['Diamonds', 'Gold', 'Silver', 'Bronze', 'Copper', 'Cyanide', 'Iron'])
# app.planet_repository.planets.append(planet_mars)
#
# print(app.send_on_mission('Mars'))
# print(app.report())
