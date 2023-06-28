def secondHighest(s):
    set_ = sorted(set([i for i in s if i.isdigit()]))
    return int(set_[-2]) if len(set_) >= 2 else -1


print(secondHighest("dfa11afd"))
print(secondHighest("ck077"))