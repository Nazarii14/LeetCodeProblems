def xorOperation(n, start):
    result = []

    for i in range(n):
        result.append(start + 2*i)

    res = result[0]
    for i in result[1:]:
        res ^= i
    return res

print(xorOperation(5, 0))
print(xorOperation(4, 3))