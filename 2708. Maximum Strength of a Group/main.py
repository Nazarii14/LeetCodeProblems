def maxStrength(nums):
    if len(nums) == 1: return nums[0]

    negatives = sorted([i for i in nums if i < 0], reverse=True)

    if len(negatives) in [0, 1] and len(negatives) + nums.count(0) == len(nums):
        return 0

    negatives = negatives[len(negatives) % 2:]
    result = 1

    for i in negatives:
        result *= i

    for i in nums:
        if i > 0:
            result *= i
    return result


print(maxStrength([3, -1, -5, 2, 5, -9]))
print(maxStrength([-4, -5, -4]))
print(maxStrength([-4, 0]))
print(maxStrength([0, 0, 0, 0, 0, 0]))
print(maxStrength([1, 1, 1, 1, 1, 1]))
print(maxStrength([-1]))
print(maxStrength([-1, -7, -7, -9, -4]))
