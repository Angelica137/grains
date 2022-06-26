from scripts.grains import grains, chessboard


def test_grains_returns_1():
    assert grains(1) == 1


def test_grains_returns_2():
    assert grains(2) == 2


def test_grains_returns_16():
    assert grains(5) == 16


def test_chessboard_returns_1():
    assert chessboard(1) == 1
