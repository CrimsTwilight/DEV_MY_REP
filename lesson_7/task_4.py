"""
4. Сделать декоратор, который измеряет время,
затраченное на выполнение декорируемой функции.
"""


from functools import wraps
from timeit import default_timer


def timeit_dec(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = default_timer()
        result = func(*args, **kwargs)
        execution_time = default_timer() - start_time

        print(f"Время выполнения для {func.__name__}: ",
              f"{execution_time:.9f} секунд.")

        return result
    return wrapper

@timeit_dec
def test_function(x):
    return x**x

test_function(5)
