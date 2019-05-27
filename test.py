def accumulate_list(iterable):
    current = 0
    lst = []
    for element in iterable:
        current += element
        lst.append(current)
    return lst


def accumulate_generator(iterable):
    current = 0
    for element in iterable:
        current += element
        yield current


# ジェネレータイテレータ
gen = accumulate_generator((1, 2, 3, 4, 5))
for e in gen:
    print(e)
# リスト
lst = accumulate_list((1, 2, 3, 4, 5))
print(lst)
