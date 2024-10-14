# Условные операторы

#color = input('Введите цвет светофора')
#
#if color == 'красный':
#   print('Остановить')

#elif color == 'желтый':
#    print('Приготовься')

#elif color == 'зеленый':
#    print('Поехали')
#else:
#    print(Неправильный цвет)


while True:
    n1 = float(input('Введите первое число'))
    action = input('Введите действие')
    n2 = float(input('Введите второе число'))

    if action == '+':
        answer = n1 + n2
        print(answer)

    elif action == '-':
        answer = n1 - n2
        print(answer)

    elif action == '*':
        answer = n1 * n2
        print(answer)

    elif action == '/' and n2 == 0:
        print('НА 0 ДЕЛИТЬ НЕЛЬЗЯ')

    elif action == '/':
        answer = n1 / n2
        print(answer)

    else:
        print('НЕПРАВИЛЬНОЕ ДЕЙСТВИЕ!!!')

