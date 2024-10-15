import random


def guess_number(range_start, range_end, attempts, initial_capital):
    number_to_guess = random.randint(range_start, range_end)
    capital = initial_capital

    print(f"Добро пожаловать в игру 'Угадай число'!")
    print(f"Вам нужно угадать число от {range_start} до {range_end}.")
    print(f"У вас есть {attempts} попыток. Ваш стартовый капитал: {capital}.")

    for attempt in range(1, attempts + 1):
        if capital <= 0:
            print("Ваш капитал закончился!")
            break

        print(f"\nПопытка {attempt}/{attempts}. Текущий капитал: {capital}")
        bet = int(input("Введите вашу ставку: "))
        if bet > capital:
            print("Ваша ставка больше, чем ваш текущий капитал.")
            continue

        guess = int(input(f"Введите число от {range_start} до {range_end}: "))

        if guess == number_to_guess:
            capital += bet
            print(f"Поздравляю! Вы угадали число {number_to_guess} и удвоили свою ставку.")
        else:
            capital -= bet
            print(f"Неверно! Загаданное число было {number_to_guess}. Вы проиграли ставку.")

        if capital <= 0:
            print("Вы проиграли все свои деньги!")
            break

    print(f"Игра окончена! Ваш итоговый капитал: {capital}")













