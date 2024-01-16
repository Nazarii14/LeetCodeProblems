def isGood(nums):
    nums = sorted(nums)
    length = len(nums)
    range_n = list(range(1, length))
    range_n.append(length - 1)
    return range_n == nums


print(isGood([2, 1, 3]))
print(isGood([2, 1, 3, 3]))
print(isGood([1, 1]))
print(isGood([3, 4, 4, 1, 2, 1]))
