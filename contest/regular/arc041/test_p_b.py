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
