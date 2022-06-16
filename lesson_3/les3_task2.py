# Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5
# (помните, что индексация начинается с нуля),
# т. к. именно в этих позициях первого массива стоят четные числа.

import random


def index(n):
    array = [random.randint(0, 30) for _ in range(n)]
    index_array = []

    for i in range(n):
        if array[i] % 2 == 0:
            index_array.append(i)
    return index_array

# "les3_task2.index(10)"
# 1000 loops, best of 5: 6.23 usec per loop

# "les3_task2.index(15)"
# 1000 loops, best of 5: 9.46 usec per loop

# "les3_task2.index(30)"
# 1000 loops, best of 5: 19.3 usec per loop

# "les3_task2.index(60)"
# 1000 loops, best of 5: 37.8 usec per


