# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива. Но если это слишком сложно,
# используйте метод сортировки, который не рассматривался на уроках (сортировка слиянием также недопустима).
# Использована Пирамидальная сортировка (или сортировка кучей)

import random

m = 5
size = 2 * m + 1
my_array = [random.randrange(0, 100) for _ in range(size)]
print(f'Исходный список: {my_array}')


def heap_func(array, len_heap, root_ind):
    big_ind = root_ind
    left_ind = (2 * root_ind) + 1
    right_ind = (2 * root_ind) + 2

    if left_ind < len_heap and array[left_ind] > array[big_ind]:
        big_ind = left_ind

    if right_ind < len_heap and array[right_ind] > array[big_ind]:
        big_ind = right_ind

    if big_ind != root_ind:
        array[root_ind], array[big_ind] = array[big_ind], array[root_ind]
        heap_func(array, len_heap, big_ind)


def heap_sort(array):

    for i in range(len(array), -1, -1):
        heap_func(array, len(array), i)

    for i in range(len(array) - 1, 0, -1):
        array[i], array[0] = array[0], array[i]
        heap_func(array, i, 0)


heap_sort(my_array)
print(f'Отсортированный список: {my_array}')
print(f'Медиана списка {my_array[m]}')
