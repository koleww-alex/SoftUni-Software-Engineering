from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    OXYGEN_USED_WHEN_TAKING_A_BREATH = 10

    def __init__(self, name: str):
        super().__init__(name)
        self.oxygen = 50

    def breathe(self):
        self.oxygen -= Geodesist.OXYGEN_USED_WHEN_TAKING_A_BREATH

