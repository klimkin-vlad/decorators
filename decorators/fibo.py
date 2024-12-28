from decorators import *

def fib1(n):
    if n < 2:
        return n
    return fib1(n-2) + fib1(n-1)
 
# измеряем время выполнения
@benchmark
def call1():
    fib1(64)

@memo
def fib2(n):
    if n < 2:
        return n
    return fib2(n-2) + fib2(n-1)
    
# измеряем время выполнения
@benchmark
def call2():
    fib2(64)

print("Без кэширования:")
call1()
print("С кэшированием:")
call2()
