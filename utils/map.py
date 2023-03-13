import pyautogui as pg
from text_colors import TextColors


class Map:
    def __init__(self, map_name=None, map_coordinates=None, map_image=None, fight_cell_next_to_mobs=None, map_cell_to_go_if_no_mobs_found=None, ):
        self.map_coordinates = map_coordinates
        self.fight_cell_next_to_mobs = fight_cell_next_to_mobs
        self.map_cell_to_go_if_no_mobs_found = map_cell_to_go_if_no_mobs_found
        self.map_image = map_image
        self.map_name = map_name

    currentMap = None

    @staticmethod
    def verifyCurrentMap():
        print(f"{TextColors.WARNING}[WARN] Verifying current map...")
        currentMap = None
        for map_obj in maps.values():
            current_map_pos = pg.locateOnScreen(
                map_obj.map_image, confidence=0.9)
            if current_map_pos:
                currentMap = map_obj
                print(
                    f"{TextColors.OKGREEN}[OK] Found map: {map_obj.map_coordinates} | Map name: {map_obj.map_name} | Cells next to mob: {map_obj.fight_cell_next_to_mobs}")
                break

        if currentMap is None:
            print(f"{TextColors.FAIL}[ERROR] Could not find any map.")

        return currentMap


maps = {
    "map1": Map(map_coordinates=[-23, 3], map_image='./img/maps/-23,3.png', fight_cell_next_to_mobs=[1198, 528], map_cell_to_go_if_no_mobs_found=[1106, 45], map_name='map1'),
    "map2": Map(map_coordinates=[-23, 2], map_image='./img/maps/-23,2.png', fight_cell_next_to_mobs=[1198, 528], map_cell_to_go_if_no_mobs_found=[1103, 42], map_name='map2')
}
