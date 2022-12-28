from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:

    def __init__(self):
        self.horses = []
        self.jockeys = []
        self.horse_races = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        if horse_name in [h.name for h in self.horses]:
            raise Exception(f'Horse {horse_name} has been already added!')

        if horse_type == 'Appaloosa':
            horse = Appaloosa(horse_name, horse_speed)
            self.horses.append(horse)
            return f'{horse_type} horse {horse_name} is added.'

        elif horse_type == 'Thoroughbred':
            horse = Thoroughbred(horse_name, horse_speed)
            self.horses.append(horse)
            return f'{horse_type} horse {horse_name} is added.'

    def add_jockey(self, jockey_name: str, age: int):
        if jockey_name in [j.name for j in self.jockeys]:
            raise Exception(f'Jockey {jockey_name} has been already added!')

        jockey = Jockey(jockey_name, age)
        self.jockeys.append(jockey)
        return f'Jockey {jockey_name} is added.'

    def create_horse_race(self, race_type: str):
        if race_type in [hr.race_type for hr in self.horse_races]:
            raise Exception(f'Race {race_type} has been already created!')

        horse_race = HorseRace(race_type)
        self.horse_races.append(horse_race)
        return f'Race {race_type} is created.'

    def __get_jockey_by_name(self, jockey_name: str):
        return [j for j in self.jockeys if j.name == jockey_name][0]

    def __get_horse_race_by_race_type(self, race_type: str):
        return [hr for hr in self.horse_races if hr.race_type == race_type][0]

    def __check_of_race_type_exists(self, race_type: str):
        if race_type not in [hr.race_type for hr in self.horse_races]:
            raise Exception(f'Race {race_type} could not be found!')

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        if jockey_name not in [j.name for j in self.jockeys]:
            raise Exception(f'Jockey {jockey_name} could not be found!')

        horse_types = ['Appaloosa', 'Thoroughbred']
        if horse_type not in horse_types or all([h.is_taken for h in self.horses if h.__class__.__name__ == horse_type]):
            raise Exception(f'Horse breed {horse_type} could not be found!')

        jockey = self.__get_jockey_by_name(jockey_name)

        if jockey.horse:
            return f'Jockey {jockey_name} already has a horse.'

        horse = [h for h in self.horses if h.__class__.__name__ == horse_type][-1]
        if not horse.is_taken:
            jockey.horse = horse
            horse.is_taken = True
            return f'Jockey {jockey_name} will ride the horse {horse.name}.'

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        self.__check_of_race_type_exists(race_type)

        if jockey_name not in [j.name for j in self.jockeys]:
            raise Exception(f'Jockey {jockey_name} could not be found!')

        jockey = self.__get_jockey_by_name(jockey_name)
        if not jockey.horse:
            raise Exception(f'Jockey {jockey_name} cannot race without a horse!')

        horse_race = self.__get_horse_race_by_race_type(race_type)
        if jockey in horse_race.jockeys:
            return f'Jockey {jockey_name} has been already added to the {race_type} race.'

        horse_race.jockeys.append(jockey)
        return f'Jockey {jockey_name} added to the {race_type} race.'

    def start_horse_race(self, race_type: str):
        self.__check_of_race_type_exists(race_type)

        horse_race = self.__get_horse_race_by_race_type(race_type)
        if len(horse_race.jockeys) < 2:
            raise Exception(f'Horse race {race_type} needs at least two participants!')

        highest_speed, jockey_winner = 0, None
        for jockey in horse_race.jockeys:
            if jockey.horse.speed > highest_speed:
                highest_speed = jockey.horse.speed
                jockey_winner = jockey

        return f"The winner of the {race_type} race, with a speed of" \
               f" {highest_speed}km/h is {jockey_winner.name}! Winner's horse: {jockey_winner.horse.name}."


horseRaceApp = HorseRaceApp()
print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))
print(horseRaceApp.add_jockey("Peter", 19))
print(horseRaceApp.add_jockey("Mariya", 21))
print(horseRaceApp.create_horse_race("Summer"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
print(horseRaceApp.start_horse_race("Summer"))
