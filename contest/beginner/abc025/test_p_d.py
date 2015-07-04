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
