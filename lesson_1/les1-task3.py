from random import randint
from random import random
from random import randrange

# Написать программу, которая генерирует в указанных пользователем границах:

# a. случайное целое число
num_int1 = int(input('Введите целое число, откуда начинается граница диапозона: '))
num_int2 = int(input('Введите целое число, где заканчивается граница диапозона: '))
num_int = randint(num_int1, num_int2)
print(num_int)

# b. случайное вещественное число
num_float1 = float(input('Введите вещественное число, откуда начинается граница диапозона: '))
num_float2 = float(input('Введите вещественное число, где заканчивается граница диапозона: '))
num_float = random() * (num_float2 - num_float1) + num_float1
print(round(num_float, 4))

# c. случайный символ
symbol1 = int(input('Введите номер буквы, откуда начинается граница диапозона: '))
symbol2 = int(input('Введите номер буквы, где заканчивается граница диапозона: '))
symbol = chr(randrange(96 + symbol1, 97 + symbol2))
print(symbol)
