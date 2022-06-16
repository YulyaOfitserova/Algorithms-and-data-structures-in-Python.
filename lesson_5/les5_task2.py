# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque

sign = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}


def sum_num(num1, num2):

    if len(num1) > len(num2):
        max_len = deque(num1)
        min_len = deque(num2)
    else:
        max_len = deque(num2)
        min_len = deque(num1)

    result = deque()
    k = 0
    while max_len:

        if min_len:
            sum_el = sign[max_len.pop()] + sign[min_len.pop()] + k
            result.appendleft(sign[sum_el % 16])
            k = sum_el // 16

        else:

            if k == 0:
                sum_el = sign[max_len.pop()]
                result.appendleft(sign[sum_el])

            else:
                sum_el = sign[max_len.pop()] + k
                result.appendleft(sign[sum_el % 16])
                k = sum_el // 16

            if k == 1:
                result.appendleft('1')

    return list(result)


def mul_num(num1, num2):

    if len(num1) > len(num2):
        max_len = deque(num1)
        min_len = deque(num2)
    else:
        max_len = deque(num2)
        min_len = deque(num1)

    result = deque()
    spam = deque([deque() for _ in range(len(min_len))])
    max_len, min_len = max_len.copy(), deque(min_len)

    for i in range(len(min_len)):
        x = sign[min_len.pop()]

        for j in range(len(max_len) - 1, -1, -1):
            spam[i].appendleft(x * sign[max_len[j]])

        for _ in range(i):
            spam[i].append(0)
    k = 0

    for _ in range(len(spam[-1])):
        res = k

        for i in range(len(spam)):
            if spam[i]:
                res += spam[i].pop()

        result.appendleft(sign[res % 16])
        k = res // 16

    if k:
        result.appendleft(sign[k])

    return list(result)


num_1 = list(input('Введите первое число: '))
num_2 = list(input('Введите второе число: '))
print(f'Сумма чисел: {sum_num(num_1, num_2)}')
print(f' Произведение чисел: {mul_num(num_1, num_2)}')


