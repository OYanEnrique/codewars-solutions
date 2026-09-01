'''
Return the first M multiples of N:
'''
def multiples(m: int, n: int | float) -> list[int] | list[float]:
    return [n * m for m in range(1, m+1)]