def removeTrailingZeros(num):
    while num[-1] == '0':
        num = num[:-1]
    return num

print(removeTrailingZeros("51230100"))
print(removeTrailingZeros("123"))
