def alternatingSubarray(self, nums):
    res = 0
    if len(nums) == 1: return 1

    for i in range(len(nums)-1):
        count = 0
        prev = nums[i]
        o = 1
        for j in range(i + 1, len(nums)):
            if nums[j] - prev == o:
                o *= -1
                count = max(count, j - i + 1)
                prev = nums[j]
            else:
                break
        res = max(res, count)
    return res if res > 0 else -1