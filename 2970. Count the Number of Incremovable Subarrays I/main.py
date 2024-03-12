def is_array_incremovable(nums):
    for i in range(1, len(nums)):
        if nums[i] <= nums[i - 1]:
            return False
    return True


def incremovableSubarrayCount(nums):
    res = 1
    for i in range(1, len(nums)):
        for j in range(len(nums) - i + 1):
            res += is_array_incremovable(nums[:j]+nums[i+j:])
            # print(nums[j:i+j])

    return res

print("1")
print(incremovableSubarrayCount([1, 2, 3, 4]))
print("2")
print(incremovableSubarrayCount([6, 5, 7, 8]))
print("3")
print(incremovableSubarrayCount([8, 7, 6, 6]))
