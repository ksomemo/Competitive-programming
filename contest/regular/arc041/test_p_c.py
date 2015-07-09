import p_c


def test_ex1():
    """右一方向のみ"""
    expected = 4
    rabbits = [
        [1, 'R'],
    ]
    actual = p_c.solve(rabbits, 5)
    assert expected == actual

def test_ex_my1_0():
    """右一方向のみ, 間隔あり"""
    expected = 5
    rabbits = [
        [1, 'R'],
        [3, 'R'],
    ]
    actual = p_c.solve(rabbits, 5)
    assert expected == actual

def test_ex_my1_1():
    """左一方向のみ"""
    expected = 4
    rabbits = [
        [3, 'L'],
        [4, 'L'],
    ]
    actual = p_c.solve(rabbits, 5)
    assert expected == actual

def test_ex_my1_2():
    """左一方向のみ, 間隔あり"""
    expected = 5
    rabbits = [
        [3, 'L'],
        [5, 'L'],
    ]
    actual = p_c.solve(rabbits, 5)
    assert expected == actual

def test_ex2():
    """左右あり左方向で終わり"""
    expected = 3
    rabbits = [
        [1, 'R'],
        [3, 'L'],
        [4, 'L'],
        [5, 'L'],
    ]
    actual = p_c.solve(rabbits, 5)
    assert expected == actual

def test_ex3():
    """左右あり右方向で終わり"""
    expected = 0
    rabbits = [
        [1, 'L'],
        [5, 'R'],
        [6, 'L'],
        [10,'R'],
    ]
    actual = p_c.solve(rabbits, 10)
    assert expected == actual

def test_ex3_my1():
    """左右あり右方向で終わり, 途中間隔あり"""
    expected = 3
    rabbits = [
        [2, 'L'],
        [4, 'L'],
        [5, 'R'],
    ]
    actual = p_c.solve(rabbits, 5)
    assert expected == actual

def test_ex3_my2():
    """左右あり右方向で終わり, 途中間隔あり(右方向へ進む)"""
    expected = 3
    rabbits = [
        [1, 'L'],
        [2, 'R'],
        [4, 'R'],
        [6, 'L'],
        [7, 'R'],
    ]
    actual = p_c.solve(rabbits, 7)
    assert expected == actual

def test_ex3_my2():
    """左右あり右方向で終わり,
    途中ぶつかるが少ないグループの間隔があるので先頭は動かなくても後ろは詰める"""
    expected = 11
    rabbits = [
        [1, 'R'],
        [2, 'R'],
        [4, 'R'],
        [6, 'R'], # 少ない方へ動く
        [8, 'L'], # 先頭は雨後ナイア
        [10, 'L'], # 先頭との間隔あるので詰める
        [11, 'L'],
        [12, 'R'],
    ]
    actual = p_c.solve(rabbits, 12)
    assert expected == actual
