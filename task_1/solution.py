import inspect


def strict(func):
    data = func.__annotations__
    return_type = data.pop("return")

    def wrapper(*args, **kwargs):
        for expected, real in zip(data.values(), args):
            if (expected != type(real)):
                raise TypeError
        value = func(*args)
        if return_type != type(value):
            raise TypeError
        return value
    return wrapper

@strict
def sum_two(a: int, b: int) -> int:
    return a + b


print(sum_two(1, 2))  # >>> 3
#print(sum_two(1, 2.4))  # >>> TypeError
print(sum_two(1, 4))