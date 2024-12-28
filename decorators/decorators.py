import time
from functools import wraps

def benchmark(func):
    """
    Декоратор, выводящий время, которое заняло выполнение декорируемой функции
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter() 
        result = func(*args, **kwargs)
        end = time.perf_counter() 
        print(f"Время выполнения функции {func.__name__}: {end - start:.6f}")
        return result
    return wrapper

def logging(func):
    """
    Декоратор, который выводит параметры с которыми была вызвана функция
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f"Функция вызвана с параметрами: {args} {kwargs}")
        return result
    return wrapper

def counter(func):
    """
    Декоратор, считающий и выводящий количество вызовов декорируемой функции
    """
    @wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        wrapper.count += 1
        print(f"Функция была вызвана: {wrapper.count} раз")
        return result
    wrapper.count = 0
    return wrapper

def memo(func):
  """
  Декоратор, запоминающий результаты исполнения функции func, чьи аргументы args должны быть хешируемыми
  """
  cache = {}

  def fmemo(*args):
      result = func(*args)
      cache[args] = result
      return result

  fmemo.cache = cache
  return fmemo
