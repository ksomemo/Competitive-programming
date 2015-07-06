import p_b


def test_ex1():
    expected = [
        [0, 0, 0],
        [0, 1, 0],
        [0, 0, 0],
    ]
    board = [
        [0, 1, 0],
        [1, 0, 1],
        [0, 1, 0],
    ]
    actual = p_b.solve(3, 3, board)
    assert expected == actual

def test_ex2():
    expected = [
        [0, 0, 0, 0],
        [0, 2, 3, 0],
        [0, 0, 0, 0],
    ]
    board = [
        [0, 2, 3, 0],
        [2, 3, 2, 3],
        [0, 2, 3, 0],
    ]
    actual = p_b.solve(3, 4, board)
    assert expected == actual

def test_ex3():
    expected = [
        [0, 0, 0, 0, 0],
        [0, 0, 1, 0, 0],
        [0, 2, 0, 3, 0],
        [0, 0, 3, 0, 0],
        [0, 0, 0, 0, 0],
    ]
    board = [
        [0, 0, 1, 0, 0],
        [0, 3, 0, 4, 0],
        [2, 0, 9, 0, 3],
        [0, 5, 0, 6, 0],
        [0, 0, 3, 0, 0],
    ]
    actual = p_b.solve(5, 5, board)
    assert expected == actual
