from dataclasses import dataclass
from typing import Literal


Side = Literal["left", "right"]

@dataclass(frozen=True)
class PlayAction:
    """Joga uma peça da mão em um dos lados da mesa."""
    tile_index: int
    side: str


@dataclass(frozen=True)
class DrawAction:
    """Compra uma peça do monte."""
    pass


@dataclass(frozen=True)
class PassAction:
    """Passa a vez quando não há jogada nem compra possível."""
    pass

Action = PlayAction | DrawAction | PassAction
