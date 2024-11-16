from decouple import config
from logic import start_game

def main():
    min_number = config('min_number', default = 1, cast=int)
    max_number = config('max_number', default = 100, cast = int)
    attempts = config('attempts', default = 5, cast = int)
    initial_capital = config('initial_capital', default = 100, cast = int)

    start_game(min_number, max_number, attempts, initial_capital)

if __name__ == "__main__":
    main()