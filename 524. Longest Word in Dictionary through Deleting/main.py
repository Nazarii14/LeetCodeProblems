def findLongestWord(s, dictionary):
    dictionary = sorted(dictionary, key=lambda x: -len(x))

    indeces = {}

    for word in dictionary:
        lst = list(set(word.split()))
        for letter in lst:
            indeces[letter] = [i for i in range(len(s)) if s[i] == letter]

    return indeces





print(findLongestWord("abpcplea", ["ale","apple","monkey","plea"]))
print(findLongestWord("abpcplea", ["a","b","c"]))
