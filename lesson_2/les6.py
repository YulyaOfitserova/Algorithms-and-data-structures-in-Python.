# Посчитать, сколько раз встречается определенная цифра
# в введенной последовательности чисел.
# Количество вводимых чисел и цифра,
# которую необходимо посчитать, задаются вводом с клавиатуры.

import random
import sys


# print(sys.version, sys.platform)
# 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] win32

# для наглядности зададим число и цифру
NUM = random.randint(1000, 100000000)
N = random.randint(0, 9)


def show_size(x, level=0):
    print("\t" * level, x.__class__, sys.getsizeof(x), x)
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for xx in x.items():
                show_size(xx, level + 1)
        elif not isinstance(x, str):
            for xx in x:
                show_size(xx, level + 1)


# Версия 1
def find_n(num=NUM, n=N):
    i = 0
    while num > 0:
        res = num % 10
        num = num // 10
        if res == n:
            i += 1
    return f'Цифра {n} встречается {i} раз(а)', show_size(NUM), show_size(res), show_size(i), show_size(num)
# <class 'int'> 28 10180681
#  <class 'int'> 28 1
#  <class 'int'> 28 2
#  <class 'int'> 24 0


# Версия 2
def num_pop(num=NUM, n=N):
    number_list = list(str(num))
    k = 0
    while number_list:
        if int(number_list.pop()) == n:
            k += 1

    return f'Цифра {n} встречается {k} раз(а)', show_size(list(str(NUM))), show_size(k)
# <class 'list'> 120 ['7', '6', '3', '8', '5', '6', '5', '1']
# 	 <class 'str'> 50 7
# 	 <class 'str'> 50 6
# 	 <class 'str'> 50 3
# 	 <class 'str'> 50 8
# 	 <class 'str'> 50 5
# 	 <class 'str'> 50 6
# 	 <class 'str'> 50 5
# 	 <class 'str'> 50 1
#  <class 'int'> 24 0


# Версия 3
def num_count(num=NUM, n=N):
    number_str = str(num)
    result = number_str.count(str(n))
    return f'Цифра {n} встречается {result} раз(а)', show_size(result), show_size(number_str)
# <class 'int'> 24 0
#  <class 'str'> 57 76385651


print(f'{NUM}')
print(f'Посчитать цифру: {N}')
print(find_n())
print(num_pop())
print(num_count())

# Вывод
# Суммарный обьем памяти для второй версии самый большой из-за списка.
# Минимальный обьем используется для типа int (1 версия),
# но из-за цикла суммарный обьем становится больше,
# чем для версии номер 3.

