from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants


class Coastline(IContainsAnimals, Identifiable):

    def __init__(self):
        IContainsAnimals.__init__(self)
        Identifiable.__init__(self)

    def add_animal(self, animal):
        try:
            if animal.aquatic:
                self.animals.append(animal)
        except AttributeError:
            raise AttributeError(
                "Cannot add non-aquatic animals to the coastline")
