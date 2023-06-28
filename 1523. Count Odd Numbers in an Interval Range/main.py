def countOdds(low, high):
    to_add = high % 2 + low % 2
    return (high - low) // 2 + to_add - 1 if to_add == 2 else (high - low) // 2 + to_add


print(countOdds(3, 7))
print(countOdds(3, 11))
print(countOdds(3, 9))
print(countOdds(3, 8))
print(countOdds(4, 5))