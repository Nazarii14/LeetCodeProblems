def searchInsert(nums, target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i
    return len(nums)

print(searchInsert([1,3,5,6], 5))
print(searchInsert([1,3,5,6], 2))
print(searchInsert([1,3,5,6], 7))
