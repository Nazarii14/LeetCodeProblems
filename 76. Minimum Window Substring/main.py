from collections import Counter
def minWindow(s, t):
    if not s or not t or len(s) < len(t):
        return ''

    t_counter = Counter(t)
    chars = len(t_counter.keys())
    s_counter = Counter()
    matches = 0
    answer = ''
    i = 0
    j = -1

    while i < len(s):
        if matches < chars:
            if j == len(s) - 1: return answer
            j += 1
            s_counter[s[j]] += 1

            if t_counter[s[j]] > 0 and s_counter[s[j]] == t_counter[s[j]]:
                matches += 1

        else:
            s_counter[s[i]] -= 1
            if t_counter[s[i]] > 0 and s_counter[s[i]] == t_counter[s[i]] - 1:
                matches -= 1
            i += 1

        if matches == chars:
            if not answer:
                answer = s[i:j + 1]
            elif (j - i + 1) < len(answer):
                answer = s[i:j + 1]
    return answer


print(minWindow("ADOBECODEBANC", "ABC"))
print(minWindow("ADOBECODEABC", "ABC"))
print(minWindow("a", "a"))
print(minWindow("a", "aa"))
