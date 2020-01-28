from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from utilities import report_maker


class River(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.name = "River"
        self.max_animals = 3
        self.max_plants = 6


    def print_list_options(self):
        string_builder = f"{self.name} ("
        total_list = super().animal_grouped_list()
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
