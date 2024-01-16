def countSegments(s):
    if s.strip() == '':
        return 0

    s = s.split(' ')
    return len([i for i in s if i != ''])


print(countSegments("Hello, my name is John"))
print(countSegments("               "))
print(countSegments("Of all the gin joints in all the towns in all the world,   "))
print(countSegments(", , , ,        a, eaefa"))