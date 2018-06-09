import A
import pytest


@pytest.mark.randomize(x=int, y=int, min_num=-(10 ** 9), max_num=10 ** 9)
def test_A(x, y):
    assert A.f(x, y) >= 0
    assert A.f(x, y) == A.editorial(x, y)


@pytest.mark.randomize(x=int, min_num=-(10 ** 9), max_num=10 ** 9)
def test_A_y0(x):
    y = 0
    assert A.f(x, y) >= 0
    assert A.f(x, y) == A.editorial(x, y)


@pytest.mark.randomize(y=int, min_num=-(10 ** 9), max_num=10 ** 9)
def test_A_x0(y):
    x = 0
    assert A.f(x, y) >= 0
    assert A.f(x, y) == A.editorial(x, y)
