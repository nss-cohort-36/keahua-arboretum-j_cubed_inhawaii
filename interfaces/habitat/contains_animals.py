class IContainsAnimals():

    def __init__(self):
        self.animals = []
        

    def animal_count(self):
        return len(self.animals)

    def add_animal(self, animal):
        self.animals.append(animal)
