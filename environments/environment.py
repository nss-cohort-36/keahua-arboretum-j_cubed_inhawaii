from interfaces import Identifiable
from interfaces import IContainsAnimals
from interfaces import IContainsPlants


class Environment(IContainsAnimals, IContainsPlants, Identifiable):

    def __init__(self, name):
        IContainsAnimals.__init__(self)
        IContainsPlants.__init__(self)
        Identifiable.__init__(self)
        
        self.name = name
