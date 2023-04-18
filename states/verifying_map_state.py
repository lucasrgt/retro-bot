from states.interface.state import State
from utils.game_checker import GameChecker
from utils.player import Player
from states.interface.tbot import TBot
from modules.screen.coordinates import Coordinates
import time
from states.interface.state import State
from states.interface.tbot import TBot
from utils.player import Player
from utils.map import MapChecker
import pyautogui as pyautogui


class VerifyingMapState(State):

    def __init__(self, context: TBot):
        self.context = context
        self.mob_found_pos = None

    def find_mob(self, sample_direction: str):
        img_path = f'./img/mobs/mob_sample_{sample_direction.lower()}.png'

        mob_pos = pyautogui.locateOnScreen(
            img_path, confidence=0.75)

        if mob_pos:
            print(f'[OK] Found mob pointing to {sample_direction}.')

            return mob_pos

        print(f'[WARN] Mob pointing to {sample_direction} not found.')

    def scan_mobs(self):

        for direction in ['TOP', 'RIGHT', 'BOTTOM', 'LEFT']:

            self.mob_found_pos = self.find_mob(
                sample_direction=direction)

            if self.mob_found_pos:
                return self.mob_found_pos

            time.sleep(1)

        return self.mob_found_pos

    def run(self):
        # Instantiate player, game checker, and window detector
        player = Player()
        game_checker = GameChecker()
        map_checker = MapChecker()

        current_map = map_checker.verify_current_map()

        mob_found_pos = self.scan_mobs()

        if mob_found_pos:

            print('Attacking mob')

            player.attack_mob(pos=Coordinates(
                mob_found_pos[0] + 5, mob_found_pos[1] + 5))

            # if game_checker.verify_if_is_fighting():
            if game_checker.verify_if_is_fighting():

                self.change_state()

        else:
            print('[WARN] No mob found. Going to the next map.')

            [x, y] = current_map.exit_to_next_map_pos.get_coordinates  # type: ignore

            pyautogui.moveTo(x, y)
            pyautogui.click()
            self.mob_found_pos = None
            print('Esperando 30 segundos para os mobs nascerem.')
            time.sleep(30)

            # TP all ip characters to the map.
            pyautogui.moveTo(953, 971)
            pyautogui.click()
            return

    def change_state(self):
        self.mob_found_pos = None
        self.context.set_state(
            self.context.fighting_state)  # type: ignore
