from agents import BaseAgent
from .controller import Controller

from domino.actions import Action
from domino.game import Game

class AgentController(Controller):

    def __init__(self, agent: BaseAgent) -> None:
        self.agent = agent

    def choose_action(self, game: Game) -> Action:
        return self.agent.choose_action(game)