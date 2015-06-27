import p_b
import pytest


@pytest.mark.parametrize('move_min, move_max, patterns, expected', [
    (5, 10, [
        ("East", 7),
        ("West", 3),
        ("West", 11),
    ], "West 8"),
    (3, 8, [
        ("West", 6),
        ("East", 3),
        ("East", 1),
    ], "0"),
    (25, 25, [
        ("East", 1),
        ("East", 1),
        ("West", 1),
        ("East", 100),
        ("West", 1),
    ], "East 25"),
])
def test_parametrized(move_min, move_max, patterns, expected):
    actual = p_b.solve(move_min, move_max, patterns)
    assert expected == actual
