from collections import deque

from .tile import Tile


class Table:
    """Representa a mesa do dominó"""

    def __init__(self):
        self.tiles_deque: deque[Tile] = deque()
        self.left_side: int | None = None
        self.right_side: int | None = None

    def __str__(self) -> str:
        if not self.tiles_deque:
            return "Mesa vazia"
        return "".join(str(tile) for tile in self.tiles_deque)

    def __contains__(self, tile: Tile) -> bool:
        return tile in self.tiles_deque

    def __getitem__(self, index: int) -> Tile:
        return self.tiles_deque[index]

    def get_sides(self) -> tuple[int | None, int | None]:
        return self.left_side, self.right_side

    def get_number_of_tiles(self) -> int:
        return len(self.tiles_deque)

    def add_first_tile(self, tile: Tile) -> None:
        if self.tiles_deque:
            raise ValueError("A mesa já possui uma peça.")
        self.left_side = tile.left_side
        self.right_side = tile.right_side
        self.tiles_deque.append(tile)

    def add_left(self, tile: Tile) -> None:
        if not self.tiles_deque:
            self.add_first_tile(tile)
            return

        if tile.right_side == self.left_side:
            pass
        elif tile.left_side == self.left_side:
            Tile.swap_tile(tile)
        else:
            raise ValueError("Essa peça não encaixa no lado esquerdo.")

        self.tiles_deque.appendleft(tile)
        self.left_side = tile.left_side

    def add_right(self, tile: Tile) -> None:
        if not self.tiles_deque:
            self.add_first_tile(tile)
            return

        if tile.left_side == self.right_side:
            pass
        elif tile.right_side == self.right_side:
            Tile.swap_tile(tile)
        else:
            raise ValueError("Essa peça não encaixa no lado direito.")

        self.tiles_deque.append(tile)
        self.right_side = tile.right_side
