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
