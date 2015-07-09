import p_c


def test_ex1():
    """右一方向のみ"""
    expected = 4
    rabbits = [
        [1, 'R'],
    ]
    actual = p_c.solve(rabbits, 5)
    assert expected == actual

def test_ex_my1():
    """左一方向のみ"""
    expected = 4
    rabbits = [
        [3, 'L'],
        [4, 'L'],
    ]
    actual = p_c.solve(rabbits, 5)
    assert expected == actual

def test_ex2():
    """左右あり左方向で終わり"""
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
    """左右あり右方向で終わり"""
    expected = 0
    rabbits = [
        [1, 'L'],
        [5, 'R'],
        [6, 'L'],
        [10,'R'],
    ]
    actual = p_c.solve(rabbits, 10)
    assert expected == actual
