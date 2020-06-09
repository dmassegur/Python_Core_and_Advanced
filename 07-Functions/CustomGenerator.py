def customgen(x,y):
    while x<y :
        yield x   ## yield adds the parameter to the end of the vector, this is creates an array
        x += 1
    return x    

result = customgen(10,30)

for i in result :
    print(i)
    