# Матрица 5x4 заполняется вводом с клавиатуры, кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки
# и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.

print('Введите значения элементов матрицы 4 на 4')
matrix = []

for m in range(4):
    matrix.append([])
    for n in range(4):
        user_number = input(f'введите элемент матрицы {m + 1} строки и {n + 1} столбца: ')
        matrix[m].append(user_number)

for line in matrix:
    all_sum = 0
    for item in line:
        all_sum = all_sum + int(item)
        print(f'{item:>2}', end='')
    print(f' |{sum:>2}')
