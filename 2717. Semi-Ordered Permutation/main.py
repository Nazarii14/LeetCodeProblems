def semiOrderedPermutation(nums):
    n = len(nums)
    i = nums.index(1)
    j = nums.index(n)
    res = i + n - 1 - j - (i > j)
    return res

print(semiOrderedPermutation([2, 1, 4, 3]))
print(semiOrderedPermutation([2, 4, 1, 3]))
print(semiOrderedPermutation([1, 3, 4, 2, 5]))
print(semiOrderedPermutation([2, 1, 3]))
print(semiOrderedPermutation([2, 3, 1]))
