# def divide(dividend, divisor):
#     result = 0
#     ddd = abs(dividend)
#     dvs = abs(divisor)
#
#     if ddd == dvs:
#         return 1 if divisor*dividend > 0 else -1
#     if dvs == 1:
#         return -dividend if divisor*dividend > 0 else dividend
#
#
#     while ddd - dvs >= 0:
#         ddd -= dvs
#         result += 1
#     return result if divisor*dividend > 0 else -result
#
# print(divide(-2147483648, -1))



def myPow(x, n):
    result = 1
    for i in range(n):
        result *= x
    return round(result, 4)

print(myPow(2.000, 10))