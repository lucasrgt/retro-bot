from states.interface.state import State
from utils.game_checker import GameChecker
from utils.player import Player
import pyautogui as pyautogui
import time


class VerifyingMapState(State):

    def __init__(self, context):
        self.context = context
        self.mob_found_pos = None

    def find_mob(self, sample_direction):
        img_path = f'./img/mobs/mob_sample_{sample_direction.lower()}.png'

        mob_pos = pyautogui.locateOnScreen(
            img_path, confidence=0.75)

        if mob_pos:
            print(f'[OK] Found mob pointing to {sample_direction}.')

            return mob_pos

        print(f'[WARN] Mob pointing to {sample_direction} not found.')

    def scan_mobs(self):
        while not self.mob_found_pos:

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

        while True:
            mob_found_pos = self.scan_mobs()

            if mob_found_pos:
                print('Attacking mob')

                player.attack_mob(pos=mob_found_pos)

                if game_checker.verify_if_is_fighting:
                    self.set_fighting_state()
            return

    def set_fighting_state(self):
        self.mob_found_pos = None
        self.context.set_state(self.context.fighting_state)
