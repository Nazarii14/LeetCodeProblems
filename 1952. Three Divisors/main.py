def isThree(n):
    if n < 4:
        return False
    divisors = []
    for i in range(2, n//2 + 1):
        if n % i == 0:
            divisors.append(i)

    return len(divisors) == 1

print(isThree(2))
print(isThree(4))
print(isThree(14))
print(isThree(41))