def maxProduct(nums):
    nums = sorted(nums)[::-1]
    return (nums[0] - 1) * (nums[1] - 1)


print(maxProduct([3, 4, 5, 2]))
