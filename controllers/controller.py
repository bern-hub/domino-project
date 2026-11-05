from abc import ABC, abstractmethod
from domino.game import Game
from domino.actions import Action

class Controller(ABC):

    @abstractmethod
    def choose_action(self, game: Game) -> Action:
        pass