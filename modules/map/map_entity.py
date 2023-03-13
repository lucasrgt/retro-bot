from modules.screen.coordinates import Coordinates
from modules.fight.fight_entity import FightEntity


class MapEntity:
    def __init__(self, map_identifier_image_path: str, map_coordinates: Coordinates, exit_to_next_map: Coordinates, exit_to_previous_map: Coordinates, fight: FightEntity):
        self._map_identifier_image_path = map_identifier_image_path
        self._map_coordinates = map_coordinates
        self._exit_to_next_map = exit_to_next_map
        self._exit_to_previous_map = exit_to_previous_map
        self._fight = fight

    @property
    def map_identifier_image_path(self):
        return self._map_identifier_image_path

    @map_identifier_image_path.setter
    def map_identifier_image_path(self, value: str):
        self._map_identifier_image_path = value

    @property
    def map_coordinates(self):
        return self._map_coordinates

    @map_coordinates.setter
    def map_coordinates(self, value: Coordinates):
        self._map_coordinates = value

    @property
    def exit_to_next_map(self):
        return self._exit_to_next_map

    @exit_to_next_map.setter
    def exit_to_next_map(self, value: Coordinates):
        self._exit_to_next_map = value

    @property
    def exit_to_previous_map(self):
        return self._exit_to_previous_map

    @exit_to_previous_map.setter
    def exit_to_previous_map(self, value: Coordinates):
        self._exit_to_previous_map = value

    @property
    def fight(self):
        return self._fight

    @fight.setter
    def fight(self, value: FightEntity):
        self._fight = value
