# В одномерном массиве найти сумму элементов, находящихся
# между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

import random

array = [random.randint(-100, 100) for _ in range(20)]

index_min = 0
index_max = 0

for i in range(20):
    if array[index_min] > array[i]:
        index_min = i
    elif array[index_max] < array[i]:
        index_max = i

a = abs(index_max - index_min)
all_sum = 0

for j in range(1, a):
    if index_min < index_max:
        all_sum = all_sum + array[index_min + j]
    else:
        all_sum = all_sum + array[index_max + j]

print(array)
print(f'минимальный элемент в списке {array[index_min]}')
print(f'максимальный элемент в списке {array[index_max]}')
print(f'{all_sum} - сумма элементов между ними')