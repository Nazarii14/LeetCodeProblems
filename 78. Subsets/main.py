def subsets(nums):
    nums = sorted(nums)
    result = [[]]
    for num in nums:
        result += [i + [num] for i in result]
    return result


print(subsets([1,2,3]))
print(subsets([0]))
