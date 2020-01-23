class IContainsPlants():

    def __init__(self):
        self.plants = []
        self.max_plants = 0

    def plant_count(self):
        return len(self.plants)

    def add_plant(self, plant):
        self.plants.append(plant)
