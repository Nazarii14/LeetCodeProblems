def mergeAlternately(word1, word2):
    min_length = len(word1) if len(word1) < len(word2) else len(word2)

    result = ""
    for i in range(min_length):
        result += word1[i] + word2[i]

    return result + word1[min_length:] + word2[min_length:]

print(mergeAlternately(word1 = "abc", word2 = "pqr"))
print(mergeAlternately(word1 = "ab", word2 = "pqrs"))
print(mergeAlternately(word1 = "abcd", word2 = "pq"))