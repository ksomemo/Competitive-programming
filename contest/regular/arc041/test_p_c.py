import p_c


def test_ex1():
    expected = 4
    rabbits = [
        [1, 'R'],
    ]
    actual = p_c.solve(rabbits, 5)
    assert expected == actual

def test_ex2():
    expected = 3
    rabbits = [
        [1, 'R'],
        [3, 'L'],
        [4, 'L'],
        [5, 'L'],
    ]
    actual = p_c.solve(rabbits, 5)
    assert expected == actual

def test_ex3():
    expected = 0
    rabbits = [
        [1, 'L'],
        [5, 'R'],
        [6, 'L'],
        [10,'R'],
    ]
    actual = p_c.solve(rabbits, 10)
    assert expected == actual
