def sortVowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vowels_in_str = [i for i in s if i.lower() in vowels]
    vowels_in_str = sorted(vowels_in_str)

    k = 0
    to_return = ""
    for i in range(len(s)):
        if s[i].lower() in vowels:
            to_return += vowels_in_str[k]
            k += 1
        else:
            to_return += s[i]
    return s

print(sortVowels('lEetcOde'))
print(sortVowels('lYmpH'))
