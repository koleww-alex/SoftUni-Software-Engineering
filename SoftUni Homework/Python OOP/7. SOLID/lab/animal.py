from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def animal_sound(self):
        ...


class Cat(Animal):

    def animal_sound(self):
        print('meow')


class Dog(Animal):

    def animal_sound(self):
        print('bark')


class Chicken(Animal):

    def animal_sound(self):
        print('cluck')


animals = [Cat(), Dog(), Chicken()]

for animal in animals:
    animal.animal_sound()
