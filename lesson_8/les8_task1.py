# На улице встретились N друзей.
# Каждый пожал руку всем остальным друзьям (по одному разу).
# Сколько рукопожатий было?

def handshake_graph(n):
    graph = [[1 for i in range(n)] for _ in range(n)]

    for i in range(len(graph)):
        graph[i][i] = 0
        print(graph[i])

    list_graph = sum(graph, [])
    result = sum(list_graph) / 2

    return result


print(f'Всего рукопожатий: {handshake_graph(4)}')
