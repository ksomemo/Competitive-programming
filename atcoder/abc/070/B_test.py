import B


def test_bがaの左():
    assert B.calc(10, 20, 0, 5) == 0


def test_bがaの右():
    assert B.calc(0, 5, 10, 20) == 0


def test_bがa包含():
    assert B.calc(10, 20, 0, 30) == 10


def test_aがb包含():
    assert B.calc(10, 20, 15, 18) == 3


def test_a_startをbが包含():
    assert B.calc(10, 20, 0, 15) == 5


def test_a_endをbが包含():
    assert B.calc(10, 20, 15, 25) == 5
