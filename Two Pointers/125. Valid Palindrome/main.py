def isPalindrome(s):
    result = "".join([i.lower() for i in s if i.isalpha() or i.isdigit()])
    return result == result[::-1]

print(isPalindrome("0p"))