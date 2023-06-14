def longestCommonPrefix(strs):
    result, min_word_length = "", min([len(i) for i in strs])

    for i in range(0, min_word_length):
        ch = strs[0][i]

        for j in strs[1:]:
            if j[i] != ch:
                return result
        result += ch
    return result


print(longestCommonPrefix(["flower","flow","flwht"]))