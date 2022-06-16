# В массиве случайных целых чисел поменять местами
# минимальный и максимальный элементы.

import random

array = [random.randint(-100, 100) for _ in range(20)]

index_min = 0
index_max = 0

for i in range(20):
    if array[index_min] > array[i]:
        index_min = i
    elif array[index_max] < array[i]:
        index_max = i

print(array)
print(f'минимальный элемент в списке {array[index_min]}')
print(f'максимальный элемент в списке {array[index_max]}')

array[index_min], array[index_max] = array[index_max], array[index_min]

print(array)
