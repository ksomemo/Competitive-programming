import p_c

def test():
    expected = (15, 80)
    points1 = [
        [0, 15, 0],
        [0, 0, 25],
        [0, 0, 0], # 計算しやすいように
    ]
    points2 = [
        [20, 10, 0],
        [0, 0, 0],
        [25, 0, 0],
    ]
    actual = p_c.solve(points1, points2)
    assert expected == actual


def test_ex2():
    expected = (72, 107)
    points1 = [
        [18, 22, 15],
        [11, 16, 17],
        [0, 0, 0],
    ]
    points2 = [
        [4, 25, 0],
        [22, 15, 0],
        [10, 4, 0],
    ]
    actual = p_c.solve(points1, points2)
    assert expected == actual
