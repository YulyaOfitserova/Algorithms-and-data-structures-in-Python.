# Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.

import random

size = 10
array = [random.randrange(-100, 100) for _ in range(size)]
print(f'Исходный список: {array}')

n = 1

while n < len(array):
    k = 0

    for i in range(len(array) - n):

        if array[i] < array[i + 1]:
            array[i], array[i + 1] = array[i + 1], array[i]
            k += 1    # считаем перестановки

    if k == 0:        # если нет перестановок
        break
    n += 1
    print(array)

print(f'Список по убыванию: {array}')
