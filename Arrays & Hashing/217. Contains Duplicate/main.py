def containsDuplicate(nums):
    return sorted(nums) != sorted(list(set(nums)))

print(containsDuplicate([1, 2, 3, 1]))