def convertToTitle(columnNumber):
    result = 0
    for i in range(len(columnNumber)):
        result += 26 ** i * (ord(columnNumber) - 64)
    result += (ord(columnNumber[-1]) - 64)
    return result


print(convertToTitle("A"))
print(convertToTitle("C"))
print(convertToTitle("AB"))
print(convertToTitle("AA"))
print(convertToTitle("ZY"))
