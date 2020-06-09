print('## Program that filters even numbers from a list: ##')

lst = [10,2,44,45,89,20]
print(lst)

result = list(filter(lambda x:x%2==0, lst))  # the lambda function is a filter to lst  ## important to convert it to list
print(result)

for i in result:
    print(i)

