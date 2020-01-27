from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from utilities import report_maker


class Grassland(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.name = "Grassland"
        self.max_animals = 22
        self.max_plants = 15

    def add_animal(self, animal):
        if self.animal_count() < self.max_animals:
            try:
                if animal.terrestrial and animal.drought_tolerant:
                    super().add_animal(animal)
                    return True
            except AttributeError:
                raise AttributeError(
                    "Cannot add non-terrestrial, or drought intolerant animals to a grassland")
        else:
            print("Too many animals!")
            return False

    def add_plant(self, plant):
        if self.plant_count() < self.max_plants:
            try:
                if plant.terrestrial and plant.drought_tolerant:
                    super().add_plant(plant)
                    return True
            except AttributeError:
                raise AttributeError(
                    "Cannot add aquatic or drought-intolerant plants to biome")
        else:
            print("Too many plants!")
            return False

    def print_list_options(self):
        string_builder = f"{self.name} ("
        total_list = super().animal_grouped_list() + super().plant_grouped_list()
        list_count = len(total_list)
        for index, item in enumerate(total_list.items()):
            string_builder += f"{item[1]} {item[0]}"
            if index + 1 != list_count:
                string_builder += ","
        string_builder += ")"
        return string_builder


    def __str__(self):
        return report_maker(
            self.name, self.id, super().animal_grouped_list(), super().plant_grouped_list())
