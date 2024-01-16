def sumOfSquares(nums):
    return sum([nums[i] * nums[i] for i in range(len(nums)) if len(nums) % (i+1) == 0])


print(sumOfSquares([1, 2, 3, 4]))
print(sumOfSquares([2, 7, 1, 19, 18, 3]))
