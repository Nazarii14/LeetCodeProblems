def hasTrailingZeros(nums: list[int]):
    return len(list(filter(lambda x: x % 2 == 0, nums))) >= 2


print(hasTrailingZeros([1, 2, 3, 4, 5]))
print(hasTrailingZeros([2, 4, 8, 16]))
print(hasTrailingZeros([1, 3, 5, 7, 9]))
