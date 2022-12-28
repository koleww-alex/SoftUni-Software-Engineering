from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    OXYGEN_USED_WHEN_TAKING_A_BREATH = 5

    def __init__(self, name: str):
        super().__init__(name)
        self.oxygen = 70

    def breathe(self):
        self.oxygen -= Biologist.OXYGEN_USED_WHEN_TAKING_A_BREATH

