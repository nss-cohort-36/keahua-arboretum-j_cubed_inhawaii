from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from utilities import report_maker
from utilities import grouped_option_string


class Grassland(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.name = "Grassland"
        self.max_animals = 22
        self.max_plants = 15


    def print_list_options(self):
        return grouped_option_string(self, super().animal_grouped_list(), super().plant_grouped_list())


    def __str__(self):
        return report_maker(
            self.name, self.id, super().animal_grouped_list(), super().plant_grouped_list())
