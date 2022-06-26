from scripts.grains import grains


def test_grains_returns_1():
    assert grains(1) == 1


def test_grains_returns_2():
    assert grains(2) == 2


def test_grains_returns_16():
    assert grains(5) == 16
