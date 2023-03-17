import pyautogui as pg
from text_colors import TextColors
from modules.map.map_list import map_list


class Map():

    current_map = None

    def verify_current_map(self):

        print(f"{TextColors.WARNING}[WARN] Verifying current map...")

        current_map = None

        for map in map_list:

            current_map_pos = pg.locateOnScreen(
                map.identifier_image_path, confidence=0.9)

            if current_map_pos:

                current_map = map

                print(
                    f"{TextColors.OKGREEN}[OK] Found map: {map.coordinates.get_coordinates} | Map name: {map.name} | Cells next to mob: {map.fight.cell_next_to_mobs.get_coordinates}")

                break

        if current_map is None:

            print(f"{TextColors.FAIL}[ERROR] Could not find any map.")

        return current_map
