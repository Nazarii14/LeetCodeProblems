def plusOne(digits):
    if digits[-1] != 9:
        digits[-1] += 1
        return digits

    index = len(digits) - 1
    while digits[index] == 9:
        digits[index] = 0
        index -= 1

    if index != -1:
        digits[index] += 1
    else:
        digits.insert(0, 1)
    return digits

print(plusOne([9, 9, 9, 9, 9, 9, 9, 9, 9]))
print(plusOne([1, 9, 9, 9, 9, 9, 9, 9, 9, 9]))
print(plusOne([1, 7, 9, 9, 9, 9, 9, 9, 9, 9]))
print(plusOne([1, 9, 9, 9, 9, 9, 9, 9, 9, 4]))

