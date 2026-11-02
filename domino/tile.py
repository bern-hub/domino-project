from __future__ import annotations


class Tile:
    """Representa uma peça do dominó"""


    def __init__(self, tuple_tile: tuple[int, int]):
        if len(tuple_tile) != 2:
            raise ValueError("Uma peça deve possuir exatamente dois lados.")

        left, right = tuple_tile
        if not (0 <= left <= 6 and 0 <= right <= 6):
            raise ValueError("Os lados devem estar entre 0 e 6.")

        self.left_side = left
        self.right_side = right

    def __str__(self) -> str:
        return f"[{self.left_side}|{self.right_side}]"

    def __repr__(self) -> str:
        return str(self)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Tile):
            return NotImplemented
        return (
            (self.left_side, self.right_side) == (other.left_side, other.right_side)
            or (self.left_side, self.right_side) == (other.right_side, other.left_side)
        )

    def __iter__(self):
        yield self.left_side
        yield self.right_side

    def __add__(self, other: object):
        if isinstance(other, Tile):
            return sum(self) + sum(other)
        return NotImplemented

    def __radd__(self, other: object):
        if isinstance(other, int):
            return other + sum(self)
        return NotImplemented

    @property
    def is_double(self) -> bool:
        return self.left_side == self.right_side

    @staticmethod
    def swap_tile(tile: "Tile") -> "Tile":
        tile.left_side, tile.right_side = tile.right_side, tile.left_side
        return tile
