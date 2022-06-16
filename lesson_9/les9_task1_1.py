# Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка.
# Требуется вернуть количество различных подстрок в этой строке.

import hashlib


def subs_count(s: str) -> int:
    str_subs = s.split(sep=None, maxsplit=-1)
    dict_subs = {}

    for j in range(len(str_subs)):
        len_sub = len(str_subs[j])
        h_subs = hashlib.sha1(str_subs[j].encode('utf-8')).hexdigest()

        count = 0
        i = 0
        while i <= int(len(s) - len_sub + 1):

            if h_subs == hashlib.sha1(s[i:i + len_sub].encode('utf-8')).hexdigest():

                if s[i:i + len_sub] == str_subs[j]:
                    count += 1
            dict_subs[str_subs[j]] = count
            i += 1

    return dict_subs


s_1 = input('Введите строку: ')
print(subs_count(s_1))
