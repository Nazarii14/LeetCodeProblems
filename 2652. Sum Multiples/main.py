def sumOfMultiples(n):
    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
            result.append(i)
    return sum(result)

print(sumOfMultiples(7))
print(sumOfMultiples(10))
print(sumOfMultiples(9))