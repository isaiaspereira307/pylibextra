from functools import singledispatch, wraps
from typing import Callable, Any


@singledispatch
def fun(s):
    return s


@fun.register(int)
def _(s):
    return s * 2
  

def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


def compose(*funcs):
    def inner(arg):
        state = arg
        for func in funcs:
            state = func(state)
        return state
    return inner


def is_bool(func: Callable) -> Callable:
    @wraps(func)
    def inner(val: Any) -> Any:
        return func(val) if isinstance(val, bool) else val
    return inner


def is_int(func: Callable) -> Callable:
    @wraps(func)
    def inner(val: Any) -> Any:
        return func(val) if isinstance(val, int) else val
    return inner

