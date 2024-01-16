def checkRecord(s):
    return not ("LLL" in s or s.count("A") > 1)

print(checkRecord("PPALLP"))