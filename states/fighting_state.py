from states.interface.state import State
from utils.fight_actions import FightActions
import time

from utils.player import Player


class FightingState(State):

    def __init__(self, context):
        self.context = context
        self.mob_find = None

    def run(self):
        fight = FightActions()
        player = Player()

        print('Sou foda to aqui')

        fight.exchange_position()
        time.sleep(1)
        fight.press_ready()
        time.sleep(2)
        fight.move_to_mobs_in_battle()
        time.sleep(2)
        fight.use_spells()
        time.sleep(1)
        fight.loop_pass()
        time.sleep(1)
        player.eatBread()
        time.sleep(1)
        self.set_verifying_map_state()

    def set_verifying_map_state(self):
        self.context.set_state(self.context.verifying_map_state)
