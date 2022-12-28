from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    OXYGEN_USED_WHEN_TAKING_A_BREATH = 15

    def __init__(self, name: str):
        super().__init__(name)
        self.oxygen = 90

    def breathe(self):
        self.oxygen -= Meteorologist.OXYGEN_USED_WHEN_TAKING_A_BREATH


