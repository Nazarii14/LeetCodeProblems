def digits_in_number(n):
    return int(max(list(str(n))))

def get_two_max(lst):
    max1 = max(lst)
    lst.remove(max1)
    max2 = max(lst)
    return max1 + max2

def maxSum(nums):
    nbd = [list() for _ in range(9)]

    for i in nums:
        j = digits_in_number(i)
        nbd[j-1].append(i)

    res = -1
    for i in range(len(nbd)):
        if len(nbd[i]) >= 2:
            res = max(res, get_two_max(nbd[i]))
    return res


print(maxSum([51, 71, 17, 24, 42]))
print(maxSum([1, 2, 3, 4]))
