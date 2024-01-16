def singleNumber(nums):
    x = 0
    for num in nums:
        x ^= num

    mask = x & -x

    ans1, ans2 = 0, 0
    for num in nums:
        if num & mask:
            ans1 ^= num
        else:
            ans2 ^= num

    return [ans1, ans2]

print(singleNumber([1,2,1,3,2,5]))
print(singleNumber([1, 0]))