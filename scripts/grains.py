def grains(square: int) -> int:
    return 2**(square-1)


def chessboard(squares: int) -> int:
    count = 0
    while squares:
        count += grains(squares)
        squares -= 1
    return count
