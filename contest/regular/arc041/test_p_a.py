import p_a
import pytest


@pytest.mark.parametrize('front, back, turn, expected', [
    (3, 2, 1, 4),
    (3, 2, 4, 3),
])
def test_examples(front, back, turn, expected):
    actual = p_a.solve(front, back, turn)
    assert expected == actual
