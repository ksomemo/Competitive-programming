import p_c

def test():
    expected = (15, 80)
    points1 = [
        [0, 15, 0],
        [0, 0, 25],
    ]
    points2 = [
        [20, 10],
        [0, 0],
        [25, 0],
    ]
    actual = p_c.solve(points1, points2)
    assert expected == actual
