def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s

    rows = [[] for row in range(numRows)]
    index, step = 0, -1

    for char in s:
        rows[index].append(char)
        if index == 0:
            step = 1
        elif index == numRows - 1:
            step = -1
        index += step

    for i in range(numRows):
        rows[i] = ''.join(rows[i])
    return ''.join(rows)


print(convert("PAYPALISHIRING", 3))
#print(convert("PAYPALISHIRING", 4))
#print(convert("PAYPALISHIRING", 5))