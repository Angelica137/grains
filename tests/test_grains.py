from scripts.grains import grains


def test_grains_returns_1():
    assert grains(1) == 1
