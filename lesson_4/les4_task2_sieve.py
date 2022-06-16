# нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное
# и возвращать соответствующее простое число.
# Решето Эратосфена

import cProfile


def sieve_erato(n):
    num = n * 4   # т.к. в сотне 26 простых, в тысяче - 168, в 10000 - 1229. умножить на 4 будет достаточно
    sieve = [i for i in range(num)]
    sieve[1] = 0

    for i in range(2, num):

        if sieve[i] != 0:
                j = i * 2
                while j < num:
                    sieve[j] = 0
                    j += i
    res = [i for i in sieve if i != 0]
    for item in res:
        if n == res.index(item) + 1:
            return item


# print(sieve_erato(5))

# "les4_task2_sieve.sieve_erato(10)"
# 1000 loops, best of 5: 6.35 usec per loop

# "les4_task2_sieve.sieve_erato(20)"
# 1000 loops, best of 5: 14.1 usec per loop

# "les4_task2_sieve.sieve_erato(50)"
# 1000 loops, best of 5: 42.8 usec per loop

# "les4_task2_sieve.sieve_erato(100)"
# 1000 loops, best of 5: 100 usec per loop

# "les4_task2_sieve.sieve_erato(1000)"
# 1000 loops, best of 5: 2.22 msec per loop

# cProfile.run('sieve_erato(10)')
# 1    0.000    0.000    0.000    0.000 les4_task2_sieve.py:9(sieve_erato)
# 10    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# cProfile.run('sieve_erato(100)')
# 1    0.000    0.000    0.000    0.000 les4_task2_sieve.py:9(sieve_erato)
# 78    0.000    0.000    0.000    0.000 {method 'index' of 'list' objects}

# cProfile.run('sieve_erato(1000)')
# 1    0.001    0.001    0.003    0.003 les4_task2_sieve.py:9(sieve_erato)
# 550    0.002    0.000    0.002    0.000 {method 'index' of 'list' object}
