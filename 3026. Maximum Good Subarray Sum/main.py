def maximumSubarraySum(nums, k):
    sum_ = nums[0]
    hm = {0: 0, 1: sum_}
    for i in range(2, len(nums) + 1):
        sum_ += nums[i - 1]
        hm[i] = sum_

    seen = {}
    res = float('-inf')

    for i in list(hm.keys())[:-1]:
        if nums[i] - k in seen:
            hm_v = seen[nums[i] - k]
            res = max(res, hm[i + 1] - hm[hm_v])
        if nums[i] + k in seen:
            hm_v = seen[nums[i] + k]
            res = max(res, hm[i + 1] - hm[hm_v])
        if nums[i] in seen:
            hm_v = seen[nums[i]]
            if hm[i] - hm[hm_v] < 0:
                seen[nums[i]] = i
        else:
            seen[nums[i]] = i
    return res if res > float('-inf') else 0


print(maximumSubarraySum([1, 2, 3, 4, 5, 6], 1))
print(maximumSubarraySum([-1, 3, 2, 4, 5], 3))
print(maximumSubarraySum([-1, -2, -3, -4], 2))
