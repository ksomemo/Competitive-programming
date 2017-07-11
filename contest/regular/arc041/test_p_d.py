import p_d


def test_ex1():
    """始点から終点まで一本道なのでYes"""
    expected = 'Yes'
    edges = [
        [1, 2, 'r'],
        [2, 3, 'b'],
        [3, 4, 'r'],
        [4, 5, 'b'],
        [5, 6, 'r'],
    ]
    actual = p_d.solve(6, 5, edges)
    assert expected == actual

def test_ex3():
    """循環している
    1--2
    |  |
    3--|
    """
    expected = 'No'
    edges = [
        [1, 2, 'b'],
        [1, 3, 'b'],
        [2, 3, 'b'],
    ]
    actual = p_d.solve(3, 3, edges)
    assert expected == actual
