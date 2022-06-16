
AB = float(input('Введите первую сторону треугольника: '))
BC = float(input('Введите вторую сторону треугольника: '))
AC = float(input('Введите третью сторону треугольника: '))

my_sum = min(AB, AC) + min(AB, BC)
if my_sum > max(AB, AC, BC):
    if AB == BC == AC:
        print('Треугольник равносторонний')
    elif AB == BC or AB == AC or AC == AB:
        print('Треугольник равнобедренный')
    else:
        print('Треугольник существует!')
else:
    print('Треугольник не существует!')
