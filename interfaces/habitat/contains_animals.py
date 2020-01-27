from collections import Counter
class IContainsAnimals():

    def __init__(self):
        self.animals = []
        self.max_animals = 0

    def animal_count(self):
        return len(self.animals)

    def animal_grouped_list(self):
        animal_names_list = [animal.species for animal in self.animals]
        return Counter(animal_names_list)

    def add_animal(self, animal):
        self.animals.append(animal)
