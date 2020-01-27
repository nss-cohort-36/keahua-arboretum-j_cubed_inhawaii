from collections import Counter
class IContainsPlants():

    def __init__(self):
        self.plants = []
        self.max_plants = 0


    def plant_count(self):
        return len(self.plants)

    def plant_grouped_list(self):
        plant_names_list = [plant.species for plant in self.plants]
        return Counter(plant_names_list)

    def add_plant(self, plant):
        self.plants.append(plant)
