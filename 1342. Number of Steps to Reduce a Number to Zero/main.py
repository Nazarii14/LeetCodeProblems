def numberOfSteps(num):
    if num == 0:
        return 0
    result = 1
    while num not in [0, 1]:
        if num % 2 == 1:
            num -= 1
            result += 1

        num /= 2
        result += 1
    return result

print(numberOfSteps(14))
print(numberOfSteps(8))
