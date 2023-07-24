def firstMissingPositive(nums):
    nums, ans = sorted(nums), 1
    for i in range(len(nums)):
        if ans == nums[i]:
            ans += 1
    return ans


print(firstMissingPositive([1,2,0]))
print(firstMissingPositive([3,4,-1,1]))
print(firstMissingPositive([7,8,9,11,12]))
