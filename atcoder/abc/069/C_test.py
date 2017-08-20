import C
import pytest


@pytest.mark.parametrize(
    "N, aa, expected", [
        (3, [1, 10, 100], "Yes"),
        (4, [1, 2, 3, 4], "No"),
        (3, [1, 4, 1], "Yes"),
        (2, [1, 1], "No"),
        (6, [2, 7, 1, 8, 2, 8], "Yes"),
    ])
def test_main(N, aa, expected):
    assert C.main(N, aa) == expected
