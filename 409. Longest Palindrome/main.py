def longestPalindrome(s):
    if s == s[::-1]:
        return s

    res = ""

    for i in range(len(s)):
        for j in range(i + 1, len(s)):
            if s[i:j] == s[i:j:-1]:
                if len(res) < j - i:
                    res = s[i:j]

    return res


print(longestPalindrome("abccccdd"))
print(longestPalindrome("a"))
print(longestPalindrome("dccaccd"))
print(longestPalindrome("dccaccdb"))
