def isFascinating(n):
    to_compare = '123456789'
    return sorted(list(str(n) + str(n*2) + str(n*3))) == list(to_compare)


print(isFascinating(192))
print(isFascinating(100))