def findDisappearedNumbers(nums):
    rng = set(range(1, len(nums) + 1))
    nums = set(sorted(nums))
    return list(rng.symmetric_difference(nums))

print(findDisappearedNumbers([4, 3, 2, 7, 8, 2, 3, 1]))
print(findDisappearedNumbers([1, 1]))
