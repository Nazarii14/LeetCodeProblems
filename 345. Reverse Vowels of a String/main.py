def reverseVowels(s):
    vowels = ['a', 'e', 'o', 'u', 'i']
    vowels_in_word = [i for i in s if i in vowels]


    word_without_vowels = []
    current_word = ""
    for i in s:
        if i in vowels:
            vowels_in_word.append(i)
            word_without_vowels.append(current_word)
            current_word = ""
        else:
            current_word += i

    result = ""
    vowels_in_word = vowels_in_word[::-1]
    if not s[0] in vowels:
        for i in range(len(word_without_vowels)):
            result += word_without_vowels[i]
            result += vowels_in_word[i]
    else:
        for i in range(len(word_without_vowels)):
            result += vowels_in_word[i]
            result += word_without_vowels[i]

    return result



print(reverseVowels("eello"))
print(reverseVowels("leetcode"))
