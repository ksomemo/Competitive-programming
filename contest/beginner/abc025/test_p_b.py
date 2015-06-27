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

def test_ex3():
    move_min = 25
    move_max = 25
    patterns = [
        ("East", 1),
        ("East", 1),
        ("West", 1),
        ("East", 100),
        ("West", 1),
    ]

    expected = "East 25"
    actual = p_b.solve(move_min, move_max, patterns)
    assert expected == actual
