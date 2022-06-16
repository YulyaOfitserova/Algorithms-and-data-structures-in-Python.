# нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное
# и возвращать соответствующее простое число.

import cProfile


def count_prime(n):
    count = 1
    number = 1
    lst_prime = [2]

    if n == 1:
        return 2

    while count < n:
        number += 2

        for num in lst_prime:
            if number % num == 0:
                break
        else:
            count += 1
            lst_prime.append(number)

    return number


# print(count_prime(7))

# "les4_task2_prime.count_prime(10)"
# 1000 loops, best of 5: 2.76 usec per loop

#  "les4_task2_prime.count_prime(20)"
# 1000 loops, best of 5: 8.68 usec per loop

# "les4_task2_prime.count_prime(50)"
# 1000 loops, best of 5: 44.8 usec per loop

# "les4_task2_prime.count_prime(100)"
# 1000 loops, best of 5: 161 usec per loop

# "les4_task2_prime.count_prime(1000)"
# 1000 loops, best of 5: 16.7 msec per loop

# cProfile.run('count_prime(10)')
# 1    0.000    0.000    0.000    0.000 les4_task2_prime.py:9(count_prime)
# 9    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run('count_prime(100)')
# 1  0.000  0.000  0.000  0.000  les4_task2_prime.py: 9(count_prime)
# 99    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}

# cProfile.run('count_prime(1000)')
# 1    0.025    0.025    0.025    0.025 les4_task2_prime.py:8(count_prime)
# 999    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
