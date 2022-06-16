# Посчитать четные и нечетные цифры введенного натурального числа.

import cProfile


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

# "les2_task2_g.num_count(12345)"
# 1000 loops, best of 5: 824 nsec per loop

# "les2_task2_g.num_count(1234567890)"
# 1000 loops, best of 5: 1.43 usec per loop

# "les2_task2_g.num_count(123456789012345)"
# 1000 loops, best of 5: 1.99 usec per loop

# "les2_task2_g.num_count(12345678901234567890)"
# 1000 loops, best of 5: 2.57 usec per loop

#cProfile.run('num_count(10234567893021)')
# 4 function calls in 0.000 seconds
#1  0.000  0.000  0.000  0.000  les2_task2_g.py: 6(num_count)


# cProfile.run('num_count(184724276519841874918659265782689571759187591856981)')
# 4 function calls in 0.000 seconds
#1  0.000  0.000  0.000  0.000  les2_task2_g.py: 6(num_count)
