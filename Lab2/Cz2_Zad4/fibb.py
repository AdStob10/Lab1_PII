def fibb_rec(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibb_rec(n - 1) + fibb_rec(n - 2)


def fibb_gen(n):
    i = 0
    while i < n:
        yield fibb_rec(i)
        i += 1


ten_fibb = [x for x in fibb_gen(10)]
print(ten_fibb)
