from .base import BaseAgent

from domino.game import Game
from domino.tile import Tile
from domino.table import Table
from domino.player import Player
from domino.actions import *

import random

class RandomAgent(BaseAgent):

    def choose_play(self, game: Game, playable: list[int]) -> Action:
        table = game.table
        player = game.current_player
        
        index = random.choice(playable)

        side = self.choose_side(player.tiles[index], table)

        return PlayAction(index, side)

    def select_side(self, tile: Tile, table: Table) -> str:
   
        return random.choice(["right", "left"])


