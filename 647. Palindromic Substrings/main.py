def is_palindrome(s):
    return s[::-1] == s


def countSubstrings(s):
    count = len(s)

    for i in range(2, len(s) + 1):
        for j in range(len(s) - i + 1):
            if is_palindrome(s[j:j + i]):
                count += 1

    return count


print(countSubstrings("aaa"))
print(countSubstrings("abc"))
