import sys

from game import Game


def main() -> None:
    Game(sys.argv[1:]).start()


if __name__ == "__main__":
    main()
