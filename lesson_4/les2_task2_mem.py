# Посчитать четные и нечетные цифры введенного натурального числа.

from functools import lru_cache
import cProfile


@lru_cache
def num_count(num):
    even = 0
    odd = 0
    for f in str(num):
        i = int(f)
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


print(num_count(12345))

# "les2_task2_mem.num_count(12345)"
# 1000 loops, best of 5: 57.4 nsec per loop


# "les2_task2_mem.num_count(1234567890)"
# 1000 loops, best of 5: 115 nsec per loop


# "les2_task2_g.num_count(123456789012345)"
# 1000 loops, best of 5: 55 nsec per loop


# "les2_task2_g.num_count(12345678901234567890)"
# 1000 loops, best of 5: 57.8 nsec per loop

#cProfile.run('num_count(1092173289467812491)')
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 les2_task2_mem.py:6(num_count)

# cProfile.run('num_count(193801924702174873284710471878137949037197375813758317581357)')
# 4 function calls in 0.000 seconds
# 1    0.000    0.000    0.000    0.000 les2_task2_mem.py:6(num_count)
