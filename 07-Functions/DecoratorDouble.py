## Decorators are functions that modify functions
def decor(fun):
    def inner():  ## will do the decoration
        result = fun()   ##!!! doesn't require inner(n) nor fun(n) because the calling fun num() is without parameter!!!
        return result*2
    return inner

def num():
    return 5

resultfun = decor(num)

print(decor(num)())
print(resultfun())


@decor
def num2():
    return 5

print(num2())

