def grains(square: int) -> int:
    if square < 0 and square > 64:
        raise ValueError("There are only 64 squares")
    return 1 << square - 1


def chessboard() -> int:
    return (1 << 64) - 1
