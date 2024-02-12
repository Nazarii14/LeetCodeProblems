def is_equilateral(lst):
    return lst[0] == lst[1] == lst[2]

def is_isosceles(lst):
    return len(set(lst)) == 2

def is_scalene(lst):
    return lst[0] != lst[1] != lst[2]

def triangle(nums):
    return (
        nums[0] + nums[1] > nums[2] or
        nums[1] + nums[2] > nums[0] or
        nums[2] + nums[0] > nums[1])

def triangleType(nums):
    if not triangle(nums):
        return "none"
    if is_scalene(nums):
        return "scalene"
    if is_isosceles(nums):
        return "isosceles"
    if is_equilateral(nums):
        return "equilateral"
