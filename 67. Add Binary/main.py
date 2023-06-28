def addBinary(a, b):
    len_a, len_b = len(a), len(b)

    if len_a < len_b:
        a = (len_b - len_a) * "0" + a
    else:
        b = (len_a - len_b) * "0" + b

    result, need_to_add = "", 0

    for i in range(len(a) - 1, -1, -1):
        if a[i] == b[i] == "1":
            need_to_add = True
            result = "0" + result
        elif a[i] == b[i] == "0":
            result = "1" + result if need_to_add else "0" + result
            need_to_add = False
        else:
            result = "0" + result if need_to_add else "1" + result
            need_to_add = False

    return result if result[0] ==  else "1" + result


print(addBinary("0", ""))
print(addBinary("11", "1"))
print(addBinary("101", "10"))
print(addBinary("1010", "1011"))