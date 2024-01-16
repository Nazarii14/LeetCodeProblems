def findComplement(num):
    length = len(str(bin(num)).replace("0b", ""))
    help = int("0b" + length*"1", 2)
    return help ^ num

print(findComplement(5))
print(findComplement(1))
print(findComplement(151))