def grains(square: int) -> int:
    if square > 64:
        raise ValueError("There are only 64 squares")
    return 2**(square-1)


def chessboard(squares: int) -> int:
    count = 0
    while squares:
        count += grains(squares)
        squares -= 1
    return count
