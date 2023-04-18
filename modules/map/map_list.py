from modules.map.map_entity import MapEntity
from modules.screen.coordinates import Coordinates
from modules.fight.fight_entity import FightEntity

map_list = [MapEntity(
    name='picles',
    identifier_image_path='./img/maps/-23,3.png',
    coordinates=Coordinates(-23, 2),
    exit_to_next_map_pos=Coordinates(884, 399),
    exit_to_previous_map_pos=Coordinates(884, 399),
    fight=FightEntity(cell_next_to_mobs=Coordinates(1206, 536),
                      before_fight_exchange_pos=Coordinates(1250, 457))
)]
