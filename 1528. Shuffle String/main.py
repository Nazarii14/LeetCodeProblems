def restoreString(s, indices):
    result = [s[i] for i in indices]
    return ''.join(result)

print(restoreString("codeleet", [4,5,6,7,0,2,1,3]))
print(restoreString("abc", [0,1,2]))
