# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.


import random

size = 10
my_array = [random.randrange(0, 50) for _ in range(size)]
print(f'Исходный список: {my_array}')


def merge_func(left_list, right_list):
    result = []
    i = 0
    j = 0

    for _ in range(len(right_list) + len(left_list)):

        if i < len(left_list) and j < len(right_list):

            if left_list[i] < right_list[j]:
                result.append(left_list[i])
                i += 1

            else:
                result.append(right_list[j])
                j += 1

        elif i == len(left_list):
            result.append(right_list[j])
            j += 1

        elif j == len(right_list):
            result.append(left_list[i])
            i += 1

    return result


def merge_sort(array):

    if len(array) < 2:
        return array

    middle = len(array) // 2
    left_list = merge_sort(array[:middle])
    right_list = merge_sort(array[middle:])

    return merge_func(left_list, right_list)


print(f'Отсортированный список: {merge_sort(my_array)}')
