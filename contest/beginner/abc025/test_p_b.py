import p_b

def test_ex1():
    move_num = 3
    move_min = 5
    move_max = 10
    patterns = [
        ("East", 7),
        ("West", 3),
        ("West", 11),
    ]

    expected = "West 8"
    actual = p_b.solve(move_num, move_min, move_max, patterns)
    assert expected == actual
