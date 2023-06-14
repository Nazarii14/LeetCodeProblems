def prec(ch):
    return 2 if ch in ["*", "/"] else 1

def evalRPN(tokens):
    stack = []
    op = ["+", "-", "*", "/"]
    for i in tokens:
        if i not in op:
            stack.append(i)
        else:
            to_append = eval(str(stack[-2])+i+str(stack[-1]))
            stack = stack[:-2]
            stack.append(to_append)
    return round(stack[0])




print(evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))