# def reverseBits(n):
#     return int((bin(n).replace("0b", "").rjust(32, "0"))[::-1], 2)

def reverseBits(n):
    reverse = 0
    for i in range(1, 32):
        reverse <<= 1
        reverse |= n & 1
        n >>= 1
    return reverse

print(reverseBits("00000010100101000001111010011100"))