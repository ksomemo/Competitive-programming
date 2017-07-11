import p_d


def test_ex1():
    board = [
        [0, 0, 15, 2, 7],
        [0, 0, 16, 1, 22],
        [20, 25, 4, 19, 0],
        [3, 23, 9, 18, 10],
        [17, 0, 5, 21, 8],
    ]
    expected = 2
    actual = p_d.solve(board)
    assert expected == actual

def test_ex2():
    board = [
        [10, 14, 13, 15, 11],
        [16, 0, 17, 0, 18],
        [0, 19, 0, 20, 9],
        [21, 12, 22, 0, 23],
        [0, 24, 0, 25, 0],
    ]
    expected = 40320
    actual = p_d.solve(board)
    assert expected == actual

    actual = p_d.solve_bit_dp(board)
    assert expected == actual

def test_ex3():
    board = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [0, 0, 0, 0, 0],
    ]
    expected = 0
    actual = p_d.solve(board)
    assert expected == actual

def test_ex4():
    board = [
        [1, 25, 2, 24, 3],
        [23, 4, 22, 5, 21],
        [6, 20, 7, 19, 8],
        [18, 9, 17, 10, 16],
        [11, 15, 12, 14, 13],
    ]
    expected = 1
    actual = p_d.solve(board)
    assert expected == actual
