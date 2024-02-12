def returnToBoundaryCount(nums):
    res = 0
    k = 0
    for i in nums:
        k += i
        res += k == 0
    return res
