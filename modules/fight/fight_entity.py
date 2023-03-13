from modules.screen.coordinates import Coordinates


class FightEntity:
    def __init__(self, cell_next_to_mobs: Coordinates):
        self._cell_next_to_mobs = cell_next_to_mobs

    @property
    def cell_next_to_mobs(self):
        return self._cell_next_to_mobs

    @cell_next_to_mobs.setter
    def cell_next_to_mobs(self, value: Coordinates):
        self._cell_next_to_mobs = value
