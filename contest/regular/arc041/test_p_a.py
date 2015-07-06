import p_a


def test_ex1():
    expected = 4
    front = 3
    back = 2
    turn = 1
    actual = p_a.solve(front, back, turn)
    assert expected == actual

def test_ex2():
    expected = 3
    front = 3
    back = 2
    turn = 4
    actual = p_a.solve(front, back, turn)
    assert expected == actual
