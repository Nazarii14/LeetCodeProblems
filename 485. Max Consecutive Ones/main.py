def findMaxConsecutiveOnes(nums):
    nums.append(0)
    res, x = 0, 0
    for i in nums:
        if i:
            x += 1
        else:
            res = max(x, res)
            x = 0
    return res