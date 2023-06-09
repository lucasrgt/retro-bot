import time
from states.interface.state import State
from states.interface.tbot import TBot
from utils.fight_actions import FightActions
from utils.player import Player
from utils.map import MapChecker


class FightingState(State):

    def __init__(self, context: TBot):
        self.context = context
        self.mob_find = None

    def run(self):
        fight = FightActions()
        player = Player()
        mapChecker = MapChecker()
        map = mapChecker.verify_current_map()

        print('[STATE] FightingState triggered.')

        fight.exchange_position(map)
        time.sleep(1)
        fight.press_ready()
        time.sleep(2)
        fight.move_to_mobs_in_battle(map)
        time.sleep(2)
        fight.use_chosen_spells(map)
        time.sleep(1)
        fight.loop_pass()
        time.sleep(1)
        player.eatBread()
        time.sleep(1)
        self.change_state()

    def change_state(self):
        self.context.set_state(
            self.context.verifying_map_state)  # type: ignore
