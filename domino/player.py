from __future__ import annotations

from .tile import Tile


class Player:
    """Representa um jogador do dominó"""

    def __init__(self, name: str, tiles: list[Tile] | None = None):
        self.name = name
        self.tiles = list(tiles) if tiles is not None else []
        self.wins = 0

    def __str__(self) -> str:
        return f"{self.name}: {self.tiles}"

    def __repr__(self) -> str:
        return str(self)

    def get_tile_points(self) -> int:
        return sum(sum(tile) for tile in self.tiles)
