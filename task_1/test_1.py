from solution import strict
import pytest

@strict
def add(a: int, b: int) -> int:
    return a + b

@strict
def mult_add(a: int, b: int, c: int, d: int) -> int:
    return a + b + c + d

@strict
def error_return(a: int, b:int) -> int:
    return str(a + b)


def test_add():
    assert add(1, 2) == 3
    assert add(a=1, b=2) == 3
    assert add(1, b=2) == 3
    with pytest.raises(TypeError):
        add(1, "a")
    with pytest.raises(TypeError):
        add(1, b="b")
    with pytest.raises(TypeError):
        add([], [])
    with pytest.raises(TypeError):
        add((), "a")

def test_mult_add():
    assert mult_add(1, 1, 1, 1) == 4
    assert mult_add(1, 1, c=1, d=1) == 4
    assert mult_add(a=1, b=1, c=1, d=1)
    with pytest.raises(TypeError):
        mult_add("a", 1, 1, 1)
    with pytest.raises(TypeError):
        mult_add(a=[], b="a", c={}, d=())

def test_return():
    with pytest.raises(TypeError):
        error_return(1, 1)
    with pytest.raises(TypeError):
        error_return(2, 3)
