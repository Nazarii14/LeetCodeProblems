def trailingZeroes(n):
    count, i = 0, 5
    while i <= n:
        count += n / i
        i *= 5
    return count

print(trailingZeroes(10))
