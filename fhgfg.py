

import random
from pprint import pprint

knb = ['камень', 'ножницы', 'бумага']

sanjar = input('Введите камень ножницы или бумага')

bot = random.choice(knb)

if bot == sanjar:
    print('Ничья')

elif (bot == 'камень' and sanjar == 'ножницы' or bot == 'ножницы' and sanjar == 'бумага'
    or bot == 'бумага' and sanjar == 'камень'):
    pprint(F'бот выбрал {bot} Я выиграл')

elif (sanjar == 'камень' and bot == 'ножницы'
    or sanjar == 'ножницы' and bot == 'бумага'
    or sanjar == 'бумага' and bot == 'камень' ):






