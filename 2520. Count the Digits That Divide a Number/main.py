def countDigits(num):
    res = 0
    str_num = str(num)
    for i in str_num:
        if num % int(i) == 0:
            res += 1
    return res

print(countDigits(7))
print(countDigits(1345))