import inspect

def before_func(values, input_types):
    for key in values.keys():
        if not isinstance(values[key], input_types[key]):
            raise TypeError(f"Parameter ( {key} ) must be {input_types[key]} not {type(values[key])}")

def after_func(expected_type, result, func_name):
    if not isinstance(result, expected_type):
        raise TypeError(f"Result of function ( {func_name} ) must be {expected_type} not {type(result)}")


def strict(func):
    sign = inspect.signature(func)
    input_types = func.__annotations__
    def wrapper(*args, **kwargs):
        values = sign.bind(*args, **kwargs).arguments
        before_func(values, input_types)
        result = func(*args, **kwargs)
        after_func(input_types['return'], result, func.__name__)
        return result

    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return str(a + b)

@strict
def sum_three(a: int, b: int, c: str) -> int:
    return a + b
