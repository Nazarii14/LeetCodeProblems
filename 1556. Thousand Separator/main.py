def thousandSeparator(n):
    if n < 1000: return str(n)

    result = str(n)[::-1]
    length = len(result)
    indeces = [i for i in range(length) if i != 0 and i % 3 == 0]
    indeces = [indeces[i] + i for i in range(len(indeces))]

    for i in indeces:
        result = result[:i] + "." + result[i:]
    return result[::-1]


print(thousandSeparator(9234234534353232343453435442323423423423422423432234324332432387))
print(thousandSeparator(1234))
print(thousandSeparator(1234567))
