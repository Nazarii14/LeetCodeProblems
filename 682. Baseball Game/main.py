def calPoints(operations):
    record = []
    for i in operations:
        if i.isdigit() or i[0] == "-":
            record.append(int(i))
        if i == "C":
            record = record[:-1]
        if i == "D":
            record.append(int(record[-1]) * 2)
        if i == "+":
            record.append(int(record[-1]) + int(record[-2]))
    return sum(record)


print(calPoints(["5","2","C","D","+"]))
print(calPoints(["5","-2","4","C","D","9","+","+"]))
print(calPoints(["1","C"]))
