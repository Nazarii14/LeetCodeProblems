def convert(s, numRows):
    if len(s) <= numRows:
        return s

    arr = [""] * numRows
    i = 0
    plus = True

    for j in s:
        if i == 0 or plus:
            plus = True
            arr[i] += j
            i += 1
        if i == numRows or not plus:
            plus = False
            i -= 1
            arr[i] += j


    return ''.join(arr)

print(convert("PAYPALISHIRING", 3))
#print(convert("PAYPALISHIRING", 4))
#print(convert("PAYPALISHIRING", 5))