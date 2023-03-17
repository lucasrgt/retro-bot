from modules.screen.coordinates import Coordinates
from modules.fight.fight_entity import FightEntity


class MapEntity:
    def __init__(self, name: str, identifier_image_path: str, coordinates: Coordinates, exit_to_next_map_pos: Coordinates, exit_to_previous_map_pos: Coordinates, fight: FightEntity):
        self._name = name
        self._identifier_image_path = identifier_image_path
        self._coordinates = coordinates
        self._exit_to_next_map_pos = exit_to_next_map_pos
        self._exit_to_previous_map_pos = exit_to_previous_map_pos
        self._fight = fight

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def identifier_image_path(self):
        return self._identifier_image_path

    @identifier_image_path.setter
    def identifier_image_path(self, value: str):
        self._identifier_image_path = value

    @property
    def coordinates(self):
        return self._coordinates

    @coordinates.setter
    def coordinates(self, value: Coordinates):
        self._coordinates = value

    @property
    def exit_to_next_map_pos(self):
        return self._exit_to_next_map_pos

    @exit_to_next_map_pos.setter
    def exit_to_next_map_pos(self, value: Coordinates):
        self._exit_to_next_map_pos = value

    @property
    def exit_to_previous_map_pos(self):
        return self._exit_to_previous_map_pos

    @exit_to_previous_map_pos.setter
    def exit_to_previous_map_pos(self, value: Coordinates):
        self._exit_to_previous_map_pos = value

    @property
    def fight(self):
        return self._fight

    @fight.setter
    def fight(self, value: FightEntity):
        self._fight = value
