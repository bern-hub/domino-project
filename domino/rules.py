from .player import Player
from .table import Table
from .tile import Tile


def get_playable_indices(player: Player, table: Table) -> list[int]:
    if not table.tiles_deque:
        return list(range(len(player.tiles)))

    left, right = table.get_sides()
    return [
        index
        for index, tile in enumerate(player.tiles)
        if tile.left_side in (left, right) or tile.right_side in (left, right)
    ]


def can_play(player: Player, table: Table) -> bool:
    return bool(get_playable_indices(player, table))


def can_place(tile: Tile, table: Table, side: str) -> bool:
    if side not in ("left", "right"):
        return False
    if not table.tiles_deque:
        return True

    endpoint = table.left_side if side == "left" else table.right_side
    return endpoint in (tile.left_side, tile.right_side)


def is_game_locked(
    players: list[Player],
    table: Table,
    stock: list[Tile] | None,
    has_stock: bool
) -> bool:
    if has_stock and stock:
        return False
    return not any(can_play(player, table) for player in players)


def get_winner(players: list[Player]) -> Player | None:
    return next((player for player in players if not player.tiles), None)


def get_player_with_fewer_points(players: list[Player]) -> Player | None:
    if not players:
        return None

    ordered = sorted(players, key=lambda player: player.get_tile_points())
    if len(ordered) > 1 and ordered[0].get_tile_points() == ordered[1].get_tile_points():
        return None
    return ordered[0]
