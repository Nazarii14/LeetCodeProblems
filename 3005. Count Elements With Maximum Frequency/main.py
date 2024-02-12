from collections import Counter

def maxFrequencyElements(nums):
    nums = Counter(nums)

    max_ = max(list(nums.values()))
    res = 0
    for i in nums:
        if nums[i] == max_:
            res += nums[i]

    return res

print(maxFrequencyElements([1, 2, 2, 1, 4, 3, ]))
print(maxFrequencyElements([1, 2, 2, 1, 4, 3, 1]))