from abc import ABC, abstractmethod


class State(ABC):

    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def change_state(self):
        pass
