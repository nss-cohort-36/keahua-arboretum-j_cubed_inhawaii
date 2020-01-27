from plants import Plant
from interfaces import ISeedProducing
from interfaces import IDroughtTolerant
from interfaces import Identifiable

class Silversword(Plant, Identifiable, IDroughtTolerant):

    def __init__(self):
        Plant.__init__(self, "Silversword", "shade", "high")
        ISeedProducing.__init__(self, 22)
        IDroughtTolerant.__init__(self)
        Identifiable.__init__(self)

    @property
    def produce_seeds(self):
        return self.__seeds_produced

    def __str__(self):
        return f'Silversword {self.id}. A drought-resistant plant. Cool.'
