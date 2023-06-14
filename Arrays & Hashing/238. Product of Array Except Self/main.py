def productExceptSelf(nums):
    if nums.count(0) > 1:
        return [0] * len(nums)
    if nums.count(0) == 1:
        multiplied_nums = 1
        for i in nums:
            if i != 0:
                multiplied_nums *= i

        return [0 if i != 0 else multiplied_nums for i in nums]
    else:
        multiplied_nums = 1
        for i in nums:
            multiplied_nums *= i

        return [int(multiplied_nums / i) for i in nums]

print(productExceptSelf([0,0]))