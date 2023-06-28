def lemonadeChange(bills):
    cash = {5:0, 10:0, 20:0}

    for i in bills:
        if i == 10:
            if cash[5] >= 1:
                cash[5] -= 1
            else: return False
        elif i == 20:
            if cash[10] >= 1 and cash[5] >= 1:
                cash[10] -= 1
                cash[5] -= 1
            elif cash[5] >= 3:
                cash[5] -= 3
            else: return False
        cash[i] += 1
    return True


#print(lemonadeChange([5,5,5,10,20]))
#print(lemonadeChange([5,5,10,10,20]))
#print(lemonadeChange([5,5,5,20,5,5,5,10,20,5,10,20,5,20,5,10,5,5,5,5]))
print(lemonadeChange([5,5,5,10,5,5,10,20,20,20]))
