s=input()  # input is string by default!
print(s)
 
s= input('Enter your name:')
print(s)
 
i=int(input('Enter your integer:'))  # converts input to integer
print(i)
print(type(i))
   
lst = [x for x in input('Enter three numbers separated by space:').split()]
lst = input('Enter three numbers separated by space:').split()  # is equivalent
print(lst)

lst = [int(x) for x in input('Enter three numbers separated by comma:').split(',')]
print(lst)

lst = [float(x) for x in input('Enter three numbers separated by comma:').split(',')]
print(lst)