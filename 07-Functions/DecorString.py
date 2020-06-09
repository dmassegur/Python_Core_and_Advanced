
def decorfun(fun):
    def inner(n):  ## will do the decoration
        result = fun(n)    ## requires inner(n) nor fun(n) because the calling fun hello(name) sends a parameter!!!
        return result+' How are you?'

    return inner

@decorfun
def hello(name):
    return 'Hello, '+name+'!'

print(hello('David'))


def hello2(name):
    return 'Hello, '+name+'!'

result = decorfun(hello2)
print(result('David'))
print(decorfun(hello2)('David'))
print(decorfun(hello2('David')))  ## not correct because decor2 returns a function, not a string!
# print(decorfun(hello2('David'))())  ## not correct either
print(hello('David'))    