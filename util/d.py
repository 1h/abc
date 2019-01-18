from functools import wraps


def logged(func):
    @wraps(func)
    def with_logging(*args, **kwargs):
        # print(func.__name__)      # 输出 'with_logging'
        # print(func.__doc__)       # 输出 None
        return func(*args, **kwargs)
    return with_logging


# 函数
@logged
def f(x):
    """does some math"""
    return x + x * x


f(1)
