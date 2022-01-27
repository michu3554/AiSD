def harmonic_sum(n: int) -> float:
    if n == 1:
        return 1.00
    return (1.00 / n) + harmonic_sum(n - 1)

n = 4
print(harmonic_sum(n))
