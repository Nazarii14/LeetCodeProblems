def finalString(s):
    to_return = ""
    for i in s:
        if i == 'i':
            to_return = to_return[::-1]
        else:
            to_return += i
    return to_return

print(finalString("string"))
print(finalString("poiinter"))