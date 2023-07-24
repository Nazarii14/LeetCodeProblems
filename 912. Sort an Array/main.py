def sortArray(nums):
    if len(nums) == 1: return nums

    result = [nums[0], nums[1]] if nums[0] < nums[1] else [nums[1], nums[0]]

    def b_search(lst, k):
        l, r, m = 0, len(lst) - 1, 0
        while l <= r:
            m = l + (r - l) // 2
            if lst[m] < k:
                l = m + 1
            elif lst[m] > k:
                r = m - 1
            else:
                return m + 1
        return min(m, r) + 1

    for i in range(2, len(nums)):
        idx = b_search(result, nums[i])
        result = result[:idx] + [nums[i]] + result[idx:]
    return result

print(sortArray([5,2,3,1]))
print(sortArray([5,1,1,2,0,0]))
print(sortArray([5,2,1,1,0,0]))
print(sortArray([0,0]))
print(sortArray([1]))
print(sortArray([1, 3, 4, 5, 6]))
print(sortArray([1, 3, 4, 3, 4]))
print(sortArray([1, 1, 1, 1, 1, 1]))


