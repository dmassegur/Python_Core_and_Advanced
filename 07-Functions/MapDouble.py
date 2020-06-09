print('## Program that maps the double of a list: ##')

lst = [2,3,4,5,6]
print(lst)

naive_double = list(map(lambda x:2*x, lst))  # applies the lambda to each term of the list.  ## you must convert the result to list!
print(naive_double)

