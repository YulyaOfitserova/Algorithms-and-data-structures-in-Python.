# Посчитать четные и нечетные цифры введенного натурального числа.

import cProfile


def num_count(num):
    n = 0
    k = 0
    while num > 0:
        number = num % 10
        num //= 10
        res = number % 2
        if res == 0:
            n += 1
        else:
            k += 1
    return n, k


# print(f'{n} четных, {k} нечетных')

# "les2_task2.num_count(12345)"
# 1000 loops, best of 5: 503 nsec per loop

# "les2_task2.num_count(1234567890)"
# 1000 loops, best of 5: 1 usec per loop

# "les2_task2.num_count(12345679012345)"
# 1000 loops, best of 5: 1.47 usec per loop

# "les2_task2.num_count(1234567901234567890)"
# 1000 loops, best of 5: 2.08 usec per loop

# cProfile.run('num_count(1874812463657)')
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 les2_task2.py:5(num_count)

# cProfile.run('num_count(120748977897947376458237928749174898174897)')
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 les2_task2.py:5(num_count)
