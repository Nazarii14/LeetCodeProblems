def letterCombinations(digits):
    dic = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'],
           4: ['g', 'h', 'i'], 5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'],
           7: ['p', 'q', 'r', 's'], 8: ['t', 'u', 'v'], 9: ['w', 'x', 'y', 'z']}

    if len(digits) == 0:
        return ""

    if len(digits) == 1:
        return dic[int(digits)]

    result = dic[int(digits[0])]
    string = ""

    for i in digits[1:]:
        new_result = []
        for j in range(len(result)):
            for k in dic[int(i)]:
                new_result.append(result[j] + k)
        result = new_result
    return result


print(letterCombinations("234"))
print(letterCombinations(""))
print(letterCombinations("2"))
