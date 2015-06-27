import p_a

def test_1():
    expected = "bc"
    actual = p_a.solve("abcde", 8)
    assert expected == actual
