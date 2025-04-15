def decor(v):
    print(v)
    def inner(n):
        return vishnu() +2

    return inner
@decor
def vishnu(n):
    return 10

print(decor(20))