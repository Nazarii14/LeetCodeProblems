def arraySign(nums):
    if 0 in nums:
        return 0

    result = 1
    for i in nums:
        result *= i

    return -1 if result < 0 else 1


print(arraySign([-1,-2,-3,-4,3,2,1]))
print(arraySign([1,5,0,2,-3]))
print(arraySign([-1,1,-1,1,-1]))