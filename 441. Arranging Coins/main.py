def arrangeCoins(n):
    stairs, result = 1, 0
    while n - stairs >= 0:
        result += 1
        n -= stairs
        stairs += 1
    return result

print(arrangeCoins(5))
print(arrangeCoins(8))
