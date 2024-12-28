from decorators import *

def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)
 
# измеряем время выполнения
@benchmark
def call1():
    fib(33)

@memo
def fib(n):
    if n < 2:
        return n
    return fib(n-2) + fib(n-1)
    
# измеряем время выполнения
@benchmark
def call2():
    fib(33)

print("С кэшированием:")
call1()
print("Без кэширования:")
call2()
