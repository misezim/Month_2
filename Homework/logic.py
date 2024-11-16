import random


def start_game(min_number, max_number, attempts, initial_capital):
    capital = initial_capital
    secret_number = random.randint(min_number, max_number)
    print(f"Initial Capital: {capital}")
    print(f"Secret number is between {min_number} and {max_number}")
    print(f"Number of attempts: {attempts}")

    for attempt in range(1, attempts + 1):
        print(f"\nRound {attempt}/{attempts}")
        print(f"Your current capital: {capital}.")

        while True:
            try:
                bet = int(input(f"Make your bet, you can bet from 1 to {capital}: "))
                if bet < 1 or bet > capital:
                    print(f"The bet should be between 1 and {capital}")
                else:
                    break
            except ValueError:
                print("Please enter int number")

        while True:
            try:
                guess = int(input(f"Quess the number between {min_number} and {max_number}: "))
                if guess < min_number or guess > max_number:
                    print(f"The number should be in range of {min_number} till {max_number}. Try again")
                else:
                    break
            except ValueError:
                print("Please enter int number")

        if guess == secret_number:
            print(f"Yes, you found the the secret number {secret_number}. Your bet is doubled")
            capital += bet
        else:
            print(f"Sorry, you didn`t found the secret number {secret_number}. You lost your bet")
            capital -= bet

        if capital <= 0:
            print("Your capital is empty. You lost")
            break

# import random
#
#
# def start_game(min_number, max_number, attempts, initial_capital):
#     capital = initial_capital
#     print(f"Добро пожаловать в игру 'Угадай число'!")
#     print(f"Начальный капитал: {capital}")
#     print(f"Диапазон чисел от {min_number} до {max_number}")
#     print(f"Количество попыток: {attempts}")
#
#     for attempt in range(attempts):
#         print(f"\nПопытка {attempt + 1}")
#
#         # Игрок делает ставку
#         try:
#             bet = float(input(f"Введите вашу ставку (текущий капитал: {capital}): "))
#             if bet <= 0 or bet > capital:
#                 print("Ставка должна быть положительной и не превышать ваш капитал.")
#                 continue
#         except ValueError:
#             print("Введите корректную ставку!")
#             continue
#
#         # Генерация случайного числа
#         number_to_guess = random.randint(min_number, max_number)
#         guess = int(input(f"Угадайте число от {min_number} до {max_number}: "))
#
#         # Проверка, угадал ли игрок
#         if guess == number_to_guess:
#             print(f"Поздравляем! Вы угадали число {number_to_guess}. Ваш капитал удваивается!")
#             capital += bet  # Удвоение ставки
#         else:
#             print(f"Увы, вы не угадали! Было число {number_to_guess}. Вы потеряли ставку.")
#             capital -= bet  # Потеря ставки
#
#         # Проверка, если капитал закончился
#         if capital <= 0:
#             print("Ваш капитал исчерпан. Игра окончена.")
#             break
#
#     # Итоговый капитал
#     print(f"\nИгра завершена. Ваш итоговый капитал: {capital}")