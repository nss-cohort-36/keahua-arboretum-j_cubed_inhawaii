from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants
from utilities import ReportMaker



class River(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        self.name = "River"
        self.max_animals = 1
        self.max_plants = 6

    def add_animal(self, animal):
        if self.animal_count() < self.max_animals:

            try:
                if animal.aquatic and animal.cell_type == "hypertonic" or animal.cell_type == "isotonic":
                    super().add_animal(animal)
                    return True
            except AttributeError:
                raise AttributeError(
                    "Cannot add non-aquatic, or saltwater animals to a river")
        else:
            print("Too many animals!")
            return False

    def add_plant(self, plant):
        if self.plant_count() < self.max_plants:
            try:
                if plant.freshwater and plant.requires_current:
                    super().add_plant(plant)
                    return True
            except AttributeError:
                raise AttributeError(
                    "Cannot add plants that require brackish water or stagnant water to a river biome")
        else:
            print("Too many plants!")
            return False

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
        return ReportMaker.report_maker(
            self.name, self.id, super().animal_grouped_list(), super().plant_grouped_list())









    


