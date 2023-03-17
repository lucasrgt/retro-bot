from abc import ABC, abstractmethod

from typing import Type

from states.interface.state import State


class TBot(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def set_state(self, state: Type[State]):
        pass
