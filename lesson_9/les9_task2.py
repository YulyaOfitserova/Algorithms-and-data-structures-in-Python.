# Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter

my_str = 'tastes differ'


class Node:

    def __init__(self, value, left=None, right=None):
        self.right = right
        self.left = left
        self.value = value


def get_code(root, codes=dict(), code=''):

    if root is None:
        return

    if isinstance(root.value, str):
        codes[root.value] = code
        return codes

    get_code(root.left, codes, code + '0')
    get_code(root.right, codes, code + '1')

    return codes


def get_tree(string):
    count_dict = Counter(string)
    print(count_dict)
    if len(count_dict) <= 1:
        node = Node(None)

        if len(count_dict) == 1:
            node.left = Node([key for key in count_dict][0])
            node.right = Node(None)

        count_dict = {node: 1}

    while len(count_dict) != 1:
        node = Node(None)
        spam = count_dict.most_common()[:-3:-1]   # идем с конца по парам

        if isinstance(spam[0][0], str):
            node.left = Node(spam[0][0])

        else:
            node.left = spam[0][0]

        if isinstance(spam[1][0], str):
            node.right = Node(spam[1][0])

        else:
            node.right = spam[1][0]

        del count_dict[spam[0][0]]
        del count_dict[spam[1][0]]
        count_dict[node] = spam[0][1] + spam[1][1]

    return [key for key in count_dict][0]


def coding(string, codes):
    res = ''

    for symbol in string:
        res += codes[symbol]

    return res


my_tree = get_tree(my_str)
codes = get_code(my_tree)
my_coding = coding(my_str, codes)

print(my_coding)
