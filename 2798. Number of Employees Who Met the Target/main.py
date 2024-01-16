def numberOfEmployeesWhoMetTarget(hours, target):
    return len([i for i in hours if i > target - 1])


print(numberOfEmployeesWhoMetTarget([0,1,2,3,4], 2))
print(numberOfEmployeesWhoMetTarget([5,1,4,2,2], 6))
