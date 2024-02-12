# def gcd(a, b):
#     return 0 if (b % a == 0 or a % b == 0) else 1
#
# def are_prosti(a, b):
#     return gcd(a, b) == 1
#
#
# def will_be_in_prosti(a, lst):
#     for i in lst:
#         if not are_prosti(i, a):
#             return False
#     return True
#
# def will_be_in_divisors(a, lst):
#     for i in lst:
#         if are_prosti(a, i):
#             return False
#     return True
#
# # print(will_be_in_divisors(3, [3, 6, 9, 12]))
#
# def divisors_in_list(a, lst):
#     return len([i for i in lst if a % i == 0])
#
#
#
# def get_divisors_by_value(value, lst):
#     lst_ = []
#
#     lst = sorted(lst)
#
#
#
#
def largest_divisible_subset(nums):
    if len(nums) <= 1:
        return nums

    dp = [1] * len(nums)
    prev_index = [-1] * len(nums)
    maxi = 0

    nums = sorted(nums)

    for i in range(1, len(nums)):
        for j in range(0, i):
            if nums[i] % nums[j] == 0 and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                prev_index[i] = j
                if dp[i] > dp[maxi]:
                    maxi = i

    result = []
    while maxi >= 0:
        result.append(nums[maxi])
        maxi = prev_index[maxi]

    return result[::-1]


print(largest_divisible_subset(nums=[1, 2, 3]))
print(largest_divisible_subset(nums=[1, 2, 4, 8]))
print(largest_divisible_subset(nums=[1, 2, 4, 8, 9, 10]))
