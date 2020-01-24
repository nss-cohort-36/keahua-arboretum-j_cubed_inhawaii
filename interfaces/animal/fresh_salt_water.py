from ..habitat import IAquatic


class IFreshSaltWater(IAquatic):

    def __init__(self):
        super().__init__()
        self.cell_type = "isotonic"
    