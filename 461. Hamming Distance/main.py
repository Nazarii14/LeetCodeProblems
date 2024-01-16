def hammingDistance(x, y):
    z = x ^ y
    z = str(bin(z)).replace("0b", "").replace("0", "")
    return len(z)

#print(hammingDistance(3, 1))
#print(hammingDistance(1, 4))
print(hammingDistance(1, 4))