def is_symmetric(num):
    if num < 100:
        return num // 10 == num % 10
    return num // 1000 + num // 100 % 10 == num // 10 % 10 + num % 10


def countSymmetricIntegers(low, high):
    if low < 10:
        low = 10
    if 100 <= low < 1000:
        low = 1000
    if high <= 10:
        return 0
    if 100 <= high < 1000:
        high = 99

    res = 0
    i = low

    while i <= high:
        res += is_symmetric(i)
        i += 1
        if i == 100:
            i = 1000

    return res

print(countSymmetricIntegers(1, 11))
print(countSymmetricIntegers(1, 100))
print(countSymmetricIntegers(1200, 1200))
print(countSymmetricIntegers(1200, 1230))
print(countSymmetricIntegers(100, 1000))
