import p_a

def test_1():
    expected = "bc"
    actual = p_a.solve("abcde", 8)
    assert expected == actual

def test_ex2():
    expected = "ue"
    actual = p_a.solve("aeiou", 22)
    assert expected == actual
