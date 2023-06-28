def kSmallestPairs(nums1, nums2, k):
    # nums = [[i, j] for i in nums1[:k] for j in nums2[:k]]
    # nums = sorted(nums, key=lambda x: x[0] + x[1])
    # return nums[:k]

    i, j = 0, 0





print(kSmallestPairs([1, 7, 11], [2, 4, 6], 3))
print(kSmallestPairs([1, 1, 2], [1, 2, 3], 2))
print(kSmallestPairs([1, 2], [3], 3))
