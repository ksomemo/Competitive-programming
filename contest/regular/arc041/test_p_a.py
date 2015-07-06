import p_a


def test_ex1():
    expected = 4
    front = 3
    back = 2
    turn = 1
    actual = p_a.solve(front, back, turn)
    assert expected == actual
