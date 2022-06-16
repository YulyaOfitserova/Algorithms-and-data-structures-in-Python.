# Написать программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
import cProfile


def test_sum(func):
    lst = [1, 3, 6, 10, 15, 21]
    for i, item in enumerate(lst):
        assert item == func(i)
        print(f'Test {i} OK')


def sum_num(n):
    return sum(range(1, sum_num(n+1)))


#test_sum(sum_num)





test_sum(sum_num(10))

