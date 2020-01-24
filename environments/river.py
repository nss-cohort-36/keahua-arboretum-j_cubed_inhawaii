from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants


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
                if animal.aquatic and animal.cell_type == "hypertonic":
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

    def __str__(self):
       return f"{self.name} has {self.plant_count()} plants and {self.animal_count()} animals!"


