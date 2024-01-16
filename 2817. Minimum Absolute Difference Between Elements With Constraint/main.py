def minAbsoluteDifference(nums, x):
    min_distance = abs(nums[0] - nums[x])
    for j in range(x, len(nums)):
        for i in range(len(nums) - j):
            s = nums[i]
            k = nums[i+j]
            min_distance = min(min_distance, abs(nums[i+j] - nums[i]))
    return min_distance


print(minAbsoluteDifference([4, 3, 2, 4], 2))
print(minAbsoluteDifference([5, 3, 2, 10, 15], 1))
print(minAbsoluteDifference([1, 2, 3, 4], 3))
