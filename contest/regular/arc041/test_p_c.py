import p_c


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
