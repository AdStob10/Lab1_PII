
def fibb_gen(n):
    i = 0
    a = 0
    b = 1


    while i < n:
        if i == 0:
            yield a

        if i == 1:
            yield b
        tmp = b
        b = a + b
        a = tmp
        yield b
        i += 1


ten_fibb = [x for x in fibb_gen(10)]
print(ten_fibb)
