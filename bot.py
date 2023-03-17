from states.fighting_state import FightingState
from states.interface.state import State
from typing import Type
from states.verifying_map_state import VerifyingMapState
from states.interface.tbot import TBot


class Bot(TBot):
    def __init__(self) -> None:
        self.verifying_map_state = VerifyingMapState(self)
        self.fighting_state = FightingState(self)

        self.state = self.verifying_map_state

    def set_state(self, state: Type[State]):
        self.state = state
