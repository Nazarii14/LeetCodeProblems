def repeatedSubstringPattern(s):
    for i in range(1, len(s) // 2 + 1):
        if len(s) % i == 0 and s[:i] * (len(s) // i) == s:
            return True
    return False



print(repeatedSubstringPattern("abab"))
print(repeatedSubstringPattern("abcabcabcabc"))
print(repeatedSubstringPattern("abc"))
print(repeatedSubstringPattern("aba"))