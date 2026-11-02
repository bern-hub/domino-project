from domino.game import Game
from interfaces.cli import CLI


def main() -> None:
    cli = CLI()
    game = Game()

    n_players, tile_count, has_stock, pull_one = cli.ask_configuration()

    while True:
        game.start_round(
            n_players=n_players,
            tile_count=tile_count,
            has_stock=has_stock,
            pull_one=pull_one,
        )
        cli.play_round(game)

        if not cli.ask_yes_no("\nDeseja jogar outra rodada? (s/n): "):
            break


if __name__ == "__main__":
    main()
