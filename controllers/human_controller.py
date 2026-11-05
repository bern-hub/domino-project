from interfaces.cli import CLI
from .controller import Controller

from domino.game import Game
from domino.actions import Action

class HumanController(Controller):

    def __init__(self, cli: CLI):
        self.cli = cli

    def choose_action(self, game: Game) -> Action:
        return self.cli.ask_action(game)
