from modules.screen.coordinates import Coordinates


class FightEntity:
    def __init__(self, cell_next_to_mobs: Coordinates, before_fight_exchange_pos: Coordinates):
        self._cell_next_to_mobs = cell_next_to_mobs
        self._before_fight_exchange_pos = before_fight_exchange_pos

    @property
    def cell_next_to_mobs(self):
        return self._cell_next_to_mobs

    @cell_next_to_mobs.setter
    def cell_next_to_mobs(self, value: Coordinates):
        self._cell_next_to_mobs = value

    @property
    def before_fight_exchange_pos(self):
        return self._before_fight_exchange_pos

    @before_fight_exchange_pos.setter
    def before_fight_exchange_pos(self, value: Coordinates):
        self._before_fight_exchange_pos = value
