# Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за четыре квартала для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий,
# чья прибыль выше среднего и ниже среднего.

from collections import defaultdict
from collections import OrderedDict

num = int(input('Введите количество предприятий: '))

profit_list = []
name_profit_dict = defaultdict(list)
av_profit_dict = {}
for i in range(num):
    name = input('Введите название предприятия: ')
    profit = input('Введите значения прибыли за 4 квартала через пробел: ')
    profit_list = profit.split()
    if len(profit_list) == 4:
        result = [float(item) for item in profit_list]
        name_profit_dict[name] = result
        av_profit = round(sum(result) / 4, 4)
        av_profit_dict[name] = av_profit
    else:
        print('Нужно ввести 4 значения!')
        break
    i += 1

print(name_profit_dict)

new_av_profit_dict = OrderedDict(sorted(av_profit_dict.items(), key=lambda x: x[1]))
print(new_av_profit_dict)

av_profit_all = round(sum(new_av_profit_dict.values()) / num, 4)
name_list_min = []
name_list_max = []
for k, v in new_av_profit_dict.items():
    if v < av_profit_all:
        name_list_min.append(k)

    elif v > av_profit_all:
        name_list_max.append(k)

print(f'{name_list_min} - предприятия с прибылью ниже среднего\n'
      f'{name_list_max} - предприятия с прибылью выше среднего')



