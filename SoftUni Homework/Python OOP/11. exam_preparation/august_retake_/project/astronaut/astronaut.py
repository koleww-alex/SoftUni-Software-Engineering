from abc import ABC, abstractmethod


class Astronaut(ABC):
    OXYGEN_USED_WHEN_TAKING_A_BREATH = 0

    def __init__(self, name: str):
        self.name = name
        self.oxygen = 0
        self.backpack = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == '':
            raise ValueError('Astronaut name cannot be empty string or whitespace!')

        self.__name = value

    @abstractmethod
    def breathe(self):
        ...

    def increase_oxygen(self, amount: int):
        self.oxygen += amount
