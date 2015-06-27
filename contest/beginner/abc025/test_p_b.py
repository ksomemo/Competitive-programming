import p_b

def test_ex1():
    move_min = 5
    move_max = 10
    patterns = [
        ("East", 7),
        ("West", 3),
        ("West", 11),
    ]

    expected = "West 8"
    actual = p_b.solve(move_min, move_max, patterns)
    assert expected == actual

def test_ex2():
    move_min = 3
    move_max = 8
    patterns = [
        ("West", 6),
        ("East", 3),
        ("East", 1),
    ]

    expected = "0"
    actual = p_b.solve(move_min, move_max, patterns)
    assert expected == actual
