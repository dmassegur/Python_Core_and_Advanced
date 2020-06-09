def factorial(n):
    if n==0 :
        result=1
        print(n)
    else :
        result = n * factorial(n-1)
        print(n)
    return result


x = 3

fact = factorial(x)

print('Factorial product of %0.1f is: %0.1f' %(x,fact))