#  Написать программу, которая обходит не взвешенный ориентированный граф без петель,
#  в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

import random


def graph_func(n, s):
    graph = [[random.randint(0, 1) for _ in range(n)] for _ in range(n)]

    for i in range(n):
        graph[i][i] = 0   # исключаем петлю

    print(graph)

    return dfs(graph, s)


visited = set()


def dfs(graph, s):
    visited.add(s)

    for i in range(len(graph)):
        if graph[s][i] == 1 and i not in visited:    # обходим непосещенные и доступные
            dfs(graph, i)                                 # и добавляем в наш путь


num = int(input('Введите число вершин графа: '))
start = int(input('Введите точку старта: '))
print(graph_func(num, start))
print(visited)
