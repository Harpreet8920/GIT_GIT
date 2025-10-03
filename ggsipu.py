def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)
def sum(n):
    if n==1:
        return 1
    else:
        return n+sum(n-1)
def fibbonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return fibbonacci(n-1)+fibbonacci(n-2)
    
def fib(n):
    a,b=0,1
    for i in range(n):
        print(a,end=" ")
        a,b=b,a+b
print(factorial(5))
print(sum(5))
print(fibbonacci(10))
fib(10)

