def isMonotonic(nums):
    return nums == sorted(nums) or nums == sorted(nums, reverse=True)
