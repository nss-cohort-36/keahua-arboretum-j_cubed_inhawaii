from .terrestrial import ITerrestrial

class IDroughtTolerant(ITerrestrial):
    def __init__(self):
        super().__init__()
        self.drought_tolerant = True
